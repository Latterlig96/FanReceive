
import datetime
from django.test import TestCase
from users.models import Customer
from matches.models import Match
from api.test.testconf import create_customer_fixture, create_customer_and_bid_fixture
from api.serializers import (CustomerSerializer, 
                             ActivitiesSerializer, 
                             MatchSerializer,
                             CustomerBidSerializer)
from django.db.models.signals import post_save
from unittest.mock import patch


class TestCustomerSerializer(TestCase):

    def setUp(self):
        self.correct_case = {
            "first_name": "TestName",
            "last_name": "TestSurname",
            "username": "TestUsername",
            "email": "testuser@gmail.com",
            "age": 20,
            "city": "Cracow",
            "password": "TestPassword123",
            "repeat_password": "TestPassword123"
        }
    
    def test_customer_serializer_create(self):
        serializer = CustomerSerializer(data=self.correct_case)
        assert serializer.is_valid()
        serializer.create(self.correct_case)
        assert Customer.objects.count() == 1
    
    def test_activity_created_on_customer_creation(self):
        serializer = CustomerSerializer(data=self.correct_case)
        assert serializer.is_valid()
        with patch("users.signals.create_activity_for_customer") as mock_signal:
            post_save.connect(mock_signal, sender=Customer, dispatch_uid="test_mock")
        serializer.create(self.correct_case)
        assert Customer.objects.count() == 1
        assert mock_signal.call_count == 1

    def test_customer_serializer_fail_create_without_first_name(self):
        self.correct_case.pop("first_name")
        serializer = CustomerSerializer(data=self.correct_case)
        assert not serializer.is_valid()

    def test_customer_serializer_fail_create_with_empty_first_name(self):
        self.correct_case.update({"first_name": ""})
        serializer = CustomerSerializer(data=self.correct_case)
        assert not serializer.is_valid()
    
    def test_customer_serializer_fail_create_with_first_name_as_none(self):
        self.correct_case.update({"first_name": None})
        serializer = CustomerSerializer(data=self.correct_case)
        assert not serializer.is_valid()
    
    def test_customer_serializer_fail_create_without_last_name(self):
        self.correct_case.pop("last_name")
        serializer = CustomerSerializer(data=self.correct_case)
        assert not serializer.is_valid()

    def test_customer_serializer_fail_create_with_empty_last_name(self):
        self.correct_case.update({"last_name": ""})
        serializer = CustomerSerializer(data=self.correct_case)
        assert not serializer.is_valid()
    
    def test_customer_serializer_fail_create_with_last_name_as_none(self):
        self.correct_case.update({"last_name": None})
        serializer = CustomerSerializer(data=self.correct_case)
        assert not serializer.is_valid()
    
    def test_customer_serializer_fail_create_without_username(self):
        self.correct_case.pop("username")
        serializer = CustomerSerializer(data=self.correct_case)
        assert not serializer.is_valid()

    def test_customer_serializer_fail_create_with_empty_username(self):
        self.correct_case.update({"username": ""})
        serializer = CustomerSerializer(data=self.correct_case)
        assert not serializer.is_valid()
    
    def test_customer_serializer_fail_create_with_username_as_none(self):
        self.correct_case.update({"username": None})
        serializer = CustomerSerializer(data=self.correct_case)
        assert not serializer.is_valid()
    
    def test_customer_serializer_fail_create_without_email(self):
        self.correct_case.pop("email")
        serializer = CustomerSerializer(data=self.correct_case)
        assert not serializer.is_valid()

    def test_customer_serializer_fail_create_with_empty_email(self):
        self.correct_case.update({"email": ""})
        serializer = CustomerSerializer(data=self.correct_case)
        assert not serializer.is_valid()
    
    def test_customer_serializer_fail_create_with_email_as_none(self):
        self.correct_case.update({"email": None})
        serializer = CustomerSerializer(data=self.correct_case)
        assert not serializer.is_valid()
    
    def test_customer_serializer_fail_create_with_invalid_email(self):
        self.correct_case.update({"email": "testtest"})
        serializer = CustomerSerializer(data=self.correct_case)
        assert not serializer.is_valid()
    
    def test_customer_serializer_fail_create_without_age(self):
        self.correct_case.pop("age")
        serializer = CustomerSerializer(data=self.correct_case)
        assert not serializer.is_valid()

    def test_customer_serializer_fail_create_with_empty_age(self):
        self.correct_case.update({"age": ""})
        serializer = CustomerSerializer(data=self.correct_case)
        assert not serializer.is_valid()
    
    def test_customer_serializer_fail_create_with_age_as_none(self):
        self.correct_case.update({"age": None})
        serializer = CustomerSerializer(data=self.correct_case)
        assert not serializer.is_valid()
    
    def test_customer_serializer_fail_create_with_age_lower_than_threshold(self):
        self.correct_case.update({"age": 16})
        serializer = CustomerSerializer(data=self.correct_case)
        assert not serializer.is_valid()
    
    def test_customer_serializer_fail_create_without_password(self):
        self.correct_case.pop("password")
        serializer = CustomerSerializer(data=self.correct_case)
        assert not serializer.is_valid()

    def test_customer_serializer_fail_create_with_empty_password(self):
        self.correct_case.update({"password": ""})
        serializer = CustomerSerializer(data=self.correct_case)
        assert not serializer.is_valid()
    
    def test_customer_serializer_fail_create_with_password_as_none(self):
        self.correct_case.update({"password": None})
        serializer = CustomerSerializer(data=self.correct_case)
        assert not serializer.is_valid()
    
    def test_customer_serializer_fail_create_without_repeat_password(self):
        self.correct_case.pop("repeat_password")
        serializer = CustomerSerializer(data=self.correct_case)
        assert not serializer.is_valid()

    def test_customer_serializer_fail_create_with_empty_repeat_password(self):
        self.correct_case.update({"repeat_password": ""})
        serializer = CustomerSerializer(data=self.correct_case)
        assert not serializer.is_valid()
    
    def test_customer_serializer_fail_create_with_repeat_password_as_none(self):
        self.correct_case.update({"repeat_password": None})
        serializer = CustomerSerializer(data=self.correct_case)
        assert not serializer.is_valid()
    
    def test_customer_serializer_fail_create_with_repeat_password_different_than_password(self):
        self.correct_case.update({"repeat_password": "SamplePassword999"})
        serializer = CustomerSerializer(data=self.correct_case)
        assert not serializer.is_valid()
    

class TestActivitiesSerializer(TestCase):

    def setUp(self):
        customer = create_customer_fixture()
        self.correct_case = {
            "customer": customer,
            "description": "Test Description"
        }
    
    def test_activity_serializer_create(self):
        serializer = ActivitiesSerializer(data=self.correct_case)
        assert serializer.is_valid()
    

class TestMatchSerializer(TestCase):

    def setUp(self):
        self.correct_case = {
            "title": "Test User vs Test User",
            "match_type": "Ekstraklasa",
            "match_result": "1:2",
            "match_schedule": datetime.datetime.today(),
            "description": "Test"   
        }
    
    def test_match_serializer_create(self):
        serializer = MatchSerializer(data=self.correct_case)
        assert serializer.is_valid()
        serializer.create(self.correct_case)
        assert Match.objects.count() == 1
    
    def test_match_serializer_fail_create_without_title(self):
        self.correct_case.pop("title")
        serializer = MatchSerializer(data=self.correct_case)
        assert not serializer.is_valid()
    
    def test_match_serializer_fail_create_with_empty_title(self):
        self.correct_case.update({"title": ""})
        serializer = MatchSerializer(data=self.correct_case)
        assert not serializer.is_valid()
    
    def test_match_serializer_fail_create_with_title_as_none(self):
        self.correct_case.update({"title": None})
        serializer = MatchSerializer(data=self.correct_case)
        assert not serializer.is_valid()
    
    def test_match_serializer_fail_create_without_match_type(self):
        self.correct_case.pop("match_type")
        serializer = MatchSerializer(data=self.correct_case)
        assert not serializer.is_valid()
    
    def test_match_serializer_fail_create_with_empty_match_type(self):
        self.correct_case.update({"match_type": ""})
        serializer = MatchSerializer(data=self.correct_case)
        assert not serializer.is_valid()
    
    def test_match_serializer_fail_create_with_match_type_as_none(self):
        self.correct_case.update({"match_type": None})
        serializer = MatchSerializer(data=self.correct_case)
        assert not serializer.is_valid()
    
    def test_match_serializer_fail_create_with_empty_match_result(self):
        self.correct_case.update({"match_result": ""})
        serializer = MatchSerializer(data=self.correct_case)
        assert not serializer.is_valid()
    
    def test_match_serializer_fail_create_with_match_result_as_none(self):
        self.correct_case.update({"match_result": None})
        serializer = MatchSerializer(data=self.correct_case)
        assert not serializer.is_valid()
    
    def test_match_serializer_fail_create_with_invalid_match_result_regex(self):
        self.correct_case.update({"match_result": "1v4"})
        serializer = MatchSerializer(data=self.correct_case)
        assert not serializer.is_valid()
    
    def test_match_serializer_fail_create_without_match_schedule(self):
        self.correct_case.pop("match_schedule")
        serializer = MatchSerializer(data=self.correct_case)
        assert not serializer.is_valid()
    
    def test_match_serializer_fail_create_with_empty_match_schedule(self):
        self.correct_case.update({"match_schedule": ""})
        serializer = MatchSerializer(data=self.correct_case)
        assert not serializer.is_valid()
    
    def test_match_serializer_fail_create_with_match_schedule_as_none(self):
        self.correct_case.update({"match_schedule": None})
        serializer = MatchSerializer(data=self.correct_case)
        assert not serializer.is_valid()
    

class TestCustomerBidSerializer(TestCase):

    def setUp(self):
        customer, bid = create_customer_and_bid_fixture()
        self.correct_case = {
            "customer": customer.pk,
            "bid": bid.pk,
            "winner": 1,
            "money_amount": 30.0
        }
    
    def test_customer_bid_serializer_create(self):
        serializer = CustomerBidSerializer(data=self.correct_case)
        assert serializer.is_valid()

    def test_match_serializer_fail_create_without_customer(self):
        self.correct_case.pop("customer")
        serializer = CustomerBidSerializer(data=self.correct_case)
        assert not serializer.is_valid()
    
    def test_match_serializer_fail_create_with_empty_customer(self):
        self.correct_case.update({"customer": ""})
        serializer = CustomerBidSerializer(data=self.correct_case)
        assert not serializer.is_valid()
    
    def test_match_serializer_fail_create_with_customer_as_none(self):
        self.correct_case.update({"customer": None})
        serializer = CustomerBidSerializer(data=self.correct_case)
        assert not serializer.is_valid()
    
    def test_match_serializer_fail_create_without_bid(self):
        self.correct_case.pop("bid")
        serializer = CustomerBidSerializer(data=self.correct_case)
        assert not serializer.is_valid()
    
    def test_match_serializer_fail_create_with_empty_bid(self):
        self.correct_case.update({"bid": ""})
        serializer = CustomerBidSerializer(data=self.correct_case)
        assert not serializer.is_valid()
    
    def test_match_serializer_fail_create_with_bid_as_none(self):
        self.correct_case.update({"bid": None})
        serializer = CustomerBidSerializer(data=self.correct_case)
        assert not serializer.is_valid()
    
    def test_match_serializer_fail_create_without_winner(self):
        self.correct_case.pop("winner")
        serializer = CustomerBidSerializer(data=self.correct_case)
        assert not serializer.is_valid()
    
    def test_match_serializer_fail_create_with_empty_winner(self):
        self.correct_case.update({"winner": ""})
        serializer = CustomerBidSerializer(data=self.correct_case)
        assert not serializer.is_valid()
    
    def test_match_serializer_fail_create_with_winner_as_none(self):
        self.correct_case.update({"winner": None})
        serializer = CustomerBidSerializer(data=self.correct_case)
        assert not serializer.is_valid()

    def test_match_serializer_fail_create_with_invalid_winner(self):
        self.correct_case.update({"winner": 3})
        serializer = CustomerBidSerializer(data=self.correct_case)
        assert not serializer.is_valid()
    
    def test_match_serializer_fail_create_without_money_amount(self):
        self.correct_case.pop("money_amount")
        serializer = CustomerBidSerializer(data=self.correct_case)
        assert not serializer.is_valid()
    
    def test_match_serializer_fail_create_with_empty_money_amount(self):
        self.correct_case.update({"money_amount": ""})
        serializer = CustomerBidSerializer(data=self.correct_case)
        assert not serializer.is_valid()
    
    def test_match_serializer_fail_create_with_money_amount_as_none(self):
        self.correct_case.update({"money_amount": None})
        serializer = CustomerBidSerializer(data=self.correct_case)
        assert not serializer.is_valid()
    
    def test_match_serializer_fail_create_with_negative_money_amount(self):
        self.correct_case.update({"money_amount": -20.0})
        serializer = CustomerBidSerializer(data=self.correct_case)
        assert not serializer.is_valid()
