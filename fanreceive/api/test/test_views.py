import json
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIRequestFactory
from api.serializers import CustomerSerializer
from api.views import CustomerRegisterAPIView
from api.test.testconf import (create_jwt_hook, 
                               create_bid_fixture, 
                               create_customer_bid_fixture_with_access_token)


class TestCustomerRegisterView(TestCase):

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
        self.factory = APIRequestFactory()
    
    def test_register_view(self):
        request = self.factory.post("/api/register", data=json.dumps(self.correct_case), content_type="application/json")
        serializer = CustomerSerializer(data=self.correct_case)
        assert serializer.is_valid()
        response = CustomerRegisterAPIView.as_view()(request)
        assert response.status_code == status.HTTP_201_CREATED
    
    def test_fail_register_without_first_name(self):
        self.correct_case.pop("first_name")
        request = self.factory.post("/api/register", data=json.dumps(self.correct_case), content_type="application/json")
        serializer = CustomerSerializer(data=self.correct_case)
        assert not serializer.is_valid()
        response = CustomerRegisterAPIView.as_view()(request)
        assert response.status_code == status.HTTP_400_BAD_REQUEST
    
    def test_fail_register_without_last_name(self):
        self.correct_case.pop("last_name")
        request = self.factory.post("/api/register", data=json.dumps(self.correct_case), content_type="application/json")
        serializer = CustomerSerializer(data=self.correct_case)
        assert not serializer.is_valid()
        response = CustomerRegisterAPIView.as_view()(request)
        assert response.status_code == status.HTTP_400_BAD_REQUEST
    
    def test_fail_register_without_username(self):
        self.correct_case.pop("username")
        request = self.factory.post("/api/register", data=json.dumps(self.correct_case), content_type="application/json")
        serializer = CustomerSerializer(data=self.correct_case)
        assert not serializer.is_valid()
        response = CustomerRegisterAPIView.as_view()(request)
        assert response.status_code == status.HTTP_400_BAD_REQUEST
    
    def test_fail_register_without_email(self):
        self.correct_case.pop("email")
        request = self.factory.post("/api/register", data=json.dumps(self.correct_case), content_type="application/json")
        serializer = CustomerSerializer(data=self.correct_case)
        assert not serializer.is_valid()
        response = CustomerRegisterAPIView.as_view()(request)
        assert response.status_code == status.HTTP_400_BAD_REQUEST
    
    def test_fail_register_with_bad_email(self):
        self.correct_case.update({"email": "Testtest"})
        request = self.factory.post("/api/register", data=json.dumps(self.correct_case), content_type="application/json")
        serializer = CustomerSerializer(data=self.correct_case)
        assert not serializer.is_valid()
        response = CustomerRegisterAPIView.as_view()(request)
        assert response.status_code == status.HTTP_400_BAD_REQUEST
    
    def test_fail_register_without_age(self):
        self.correct_case.pop("age")
        request = self.factory.post("/api/register", data=json.dumps(self.correct_case), content_type="application/json")
        serializer = CustomerSerializer(data=self.correct_case)
        assert not serializer.is_valid()
        response = CustomerRegisterAPIView.as_view()(request)
        assert response.status_code == status.HTTP_400_BAD_REQUEST
    
    def test_fail_register_with_age_below_threshold(self):
        self.correct_case.update({"age": 16})
        request = self.factory.post("/api/register", data=json.dumps(self.correct_case), content_type="application/json")
        serializer = CustomerSerializer(data=self.correct_case)
        assert not serializer.is_valid()
        response = CustomerRegisterAPIView.as_view()(request)
        assert response.status_code == status.HTTP_400_BAD_REQUEST
    
    def test_fail_register_without_password(self):
        self.correct_case.pop("password")
        request = self.factory.post("/api/register", data=json.dumps(self.correct_case), content_type="application/json")
        serializer = CustomerSerializer(data=self.correct_case)
        assert not serializer.is_valid()
        response = CustomerRegisterAPIView.as_view()(request)
        assert response.status_code == status.HTTP_400_BAD_REQUEST
    
    def test_fail_register_without_repeated_password(self):
        self.correct_case.pop("repeat_password")
        request = self.factory.post("/api/register", data=json.dumps(self.correct_case), content_type="application/json")
        serializer = CustomerSerializer(data=self.correct_case)
        assert not serializer.is_valid()
        response = CustomerRegisterAPIView.as_view()(request)
        assert response.status_code == status.HTTP_400_BAD_REQUEST
    
    def test_fail_register_with_invalid_repeat_password(self):
        self.correct_case.pop("repeat_password")
        request = self.factory.post("/api/register", data=json.dumps(self.correct_case), content_type="application/json")
        serializer = CustomerSerializer(data=self.correct_case)
        assert not serializer.is_valid()
        response = CustomerRegisterAPIView.as_view()(request)
        assert response.status_code == status.HTTP_400_BAD_REQUEST
    

class TestCustomerSettingsAPIView(TestCase):

    def setUp(self):
        self.access_token = create_jwt_hook(self.client)
        
    def test_settings_view(self):
        header = "Bearer %s" %(self.access_token)
        response = self.client.get("/api/customer/1/settings/", 
                                   content_type="application/json", 
                                   HTTP_AUTHORIZATION=header)
        assert response.status_code == status.HTTP_200_OK
    
class TestListBidAPIView(TestCase):

    def setUp(self):
        bid = create_bid_fixture()
        self.access_token = create_jwt_hook(self.client)
    
    def test_list_bid_view(self):
        header = "Bearer %s" %(self.access_token)
        response = self.client.get("/api/bids/", 
                                   content_type="application/json", 
                                   HTTP_AUTHORIZATION=header)
        assert response.status_code == status.HTTP_200_OK


class TestCreateBidAPIView(TestCase):

    def setUp(self):
        bid = create_bid_fixture()
        self.access_token = create_jwt_hook(self.client)
        self.data = {
            "customer": 1,
            "bid": 1,
            "winner": 1,
            "money_amount": 30.0
        }
    
    def test_create_bid_view(self):
        header = "Bearer %s" %(self.access_token)
        response = self.client.post("/api/bid/create",
                                   data=self.data, 
                                   content_type="application/json", 
                                   HTTP_AUTHORIZATION=header)

        assert response.status_code == status.HTTP_201_CREATED
    
    def test_create_fail_bid_view_without_customer(self):
        self.data.pop("customer")
        header = "Bearer %s" %(self.access_token)
        response = self.client.post("/api/bid/create",
                                   data=self.data, 
                                   content_type="application/json", 
                                   HTTP_AUTHORIZATION=header)

        assert response.status_code == status.HTTP_400_BAD_REQUEST
    
    def test_create_fail_bid_view_without_bid(self):
        self.data.pop("bid")
        header = "Bearer %s" %(self.access_token)
        response = self.client.post("/api/bid/create",
                                   data=self.data, 
                                   content_type="application/json", 
                                   HTTP_AUTHORIZATION=header)
                                   
        assert response.status_code == status.HTTP_400_BAD_REQUEST
    
    def test_create_fail_bid_view_without_winner(self):
        self.data.pop("winner")
        header = "Bearer %s" %(self.access_token)
        response = self.client.post("/api/bid/create",
                                   data=self.data, 
                                   content_type="application/json", 
                                   HTTP_AUTHORIZATION=header)
                                   
        assert response.status_code == status.HTTP_400_BAD_REQUEST
    
    def test_create_fail_bid_view_with_wrong_winner(self):
        self.data.update({"winner": 5})
        header = "Bearer %s" %(self.access_token)
        response = self.client.post("/api/bid/create",
                                   data=self.data, 
                                   content_type="application/json", 
                                   HTTP_AUTHORIZATION=header)
                                   
        assert response.status_code == status.HTTP_400_BAD_REQUEST
    
    def test_create_fail_bid_view_without_money_amount(self):
        self.data.pop("money_amount")
        header = "Bearer %s" %(self.access_token)
        response = self.client.post("/api/bid/create",
                                   data=self.data, 
                                   content_type="application/json", 
                                   HTTP_AUTHORIZATION=header)
                                   
        assert response.status_code == status.HTTP_400_BAD_REQUEST
    
    def test_create_fail_bid_view_with_negative_money_amount(self):
        self.data.update({"money_amount": -20.0})
        header = "Bearer %s" %(self.access_token)
        response = self.client.post("/api/bid/create",
                                   data=self.data, 
                                   content_type="application/json", 
                                   HTTP_AUTHORIZATION=header)
                                   
        assert response.status_code == status.HTTP_400_BAD_REQUEST
    

class TestRetrieveMatchAPIView(TestCase):

    def setUp(self):
        bid = create_bid_fixture()
        self.access_token = create_jwt_hook(self.client)
    
    def test_match_retrieve_view(self):
        header = "Bearer %s" %(self.access_token)
        response = self.client.get("/api/match/1/description",
                                   content_type="application/json", 
                                   HTTP_AUTHORIZATION=header)

        assert response.status_code == status.HTTP_200_OK
    

class TestBidResultsAPIView(TestCase):

    def setUp(self):
        self.customer_bid, self.access_token = create_customer_bid_fixture_with_access_token(self.client)

    def test_customer_bid_view(self):
        header = "Bearer %s" %(self.access_token)
        response = self.client.get("/api/customer/1/bids/1/result",
                                   content_type="application/json", 
                                   HTTP_AUTHORIZATION=header)
                                   
        assert response.status_code == status.HTTP_200_OK
