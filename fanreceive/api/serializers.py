from rest_framework import serializers
from users.models import Customer, Activities
from matches.models import Match
from bid.models import CustomerBid, Bid
from django.contrib.auth.hashers import make_password
from rest_framework.exceptions import ValidationError


class CustomerSerializer(serializers.ModelSerializer):

    email = serializers.EmailField(max_length=100, required=True)
    password = serializers.CharField(max_length=100, required=True, write_only=True)
    repeat_password = serializers.CharField(max_length=100, required=True, write_only=True)

    class Meta:
        model = Customer
        fields = ("username",
                  "first_name", 
                  "last_name", 
                  "email", 
                  "age", 
                  "password",
                  "repeat_password"
            )

    def validate(self, data):
        if data["password"] != data["repeat_password"]:
            raise serializers.ValidationError("Password's don't match, please try again")
        return data

    def create(self, validated_data):
        validated_data.pop("repeat_password")
        customer = Customer(**validated_data)
        customer.set_password(validated_data["password"])
        customer.save()
        return customer

class ActivitiesSerializer(serializers.ModelSerializer):

    customer = serializers.PrimaryKeyRelatedField(many=False, read_only=True)

    class Meta:
        model = Activities
        fields = ("customer", "description")

class CustomerSettingsSerializer(serializers.ModelSerializer):

    email = serializers.EmailField(max_length=100, required=True)

    class Meta:
        model = Customer
        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
            "age"
        )


class MatchSerializer(serializers.ModelSerializer):
    
    image = serializers.ImageField(required=False)
    
    class Meta:
        model = Match
        fields = (
            "title",
            "match_type",
            "match_result",
            "match_schedule",
            "description",
            "image",
        )


class BidSerializer(serializers.ModelSerializer):

    match = serializers.PrimaryKeyRelatedField(many=False, 
                                               required=True, 
                                               queryset=Bid.objects.all())
    
    class Meta:
        model = Bid
        fields = ("match", "course")


class CustomerBidSerializer(serializers.ModelSerializer):

    customer = serializers.PrimaryKeyRelatedField(many=False, 
                                                  required=True,
                                                  queryset=Customer.objects.all())
    bid = serializers.PrimaryKeyRelatedField(many=False, 
                                             required=True,
                                             queryset=Bid.objects.all())
    winner = serializers.IntegerField(required=True)
    money_amount = serializers.DecimalField(max_digits=10, 
                                            decimal_places=2, 
                                            min_value=0, 
                                            required=True)

    class Meta:
        model = CustomerBid
        fields = ("customer", "bid", "winner", "money_amount")

    def validate(self, data):
        winner = data["winner"]
        if winner not in [0, 1]:
            raise ValidationError("Winner field should be equals 0 (if you think first team will win) or 1")
        if CustomerBid.objects.filter(customer=data["customer"], bid=data["bid"]).exists():
            raise ValidationError("You can't bid two times on the same match")
        if data["money_amount"] == 0:
            raise ValidationError("You can't bet on match without money")
        return data

    def create(self, validated_data):
        return CustomerBid.objects.create(**validated_data)
