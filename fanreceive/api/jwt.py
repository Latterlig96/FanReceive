from users.models import Customer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class EmailObtainPairSerializer(TokenObtainPairSerializer):
    username_field = Customer.EMAIL_FIELD

class EmailTokenObtainPairView(TokenObtainPairView):
    serializer_class = EmailObtainPairSerializer
