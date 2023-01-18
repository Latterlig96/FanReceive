import datetime
from users.models import Customer
from matches.models import Match
from bid.models import Bid, CustomerBid


def create_customer_fixture():
    correct_case = {
            "first_name": "TestName",
            "last_name": "TestSurname",
            "username": "TestUsername",
            "email": "testuser@gmail.com",
            "age": 20,
            "city": "Cracow",
            "password": "TestPassword123"
        }
    customer = Customer.objects.create_user(**correct_case)
    customer.is_active = True
    customer.set_password = correct_case["password"]
    customer.save()
    return customer

def create_match_fixture():
    correct_case = {
            "title": "Test User vs Test User",
            "match_type": "Ekstraklasa",
            "match_result": "1:2",
            "match_schedule": datetime.date.today(),
            "description": "Test"   
        }
    return Match.objects.create(**correct_case)

def create_customer_and_bid_fixture():
    customer = create_customer_fixture()
    match = create_match_fixture()
    return customer, Bid.objects.create(match=match, course="1.0v5.0")

def create_bid_fixture():
    match = create_match_fixture()
    return Bid.objects.create(match=match, course="1.0v5.0")

def create_jwt_hook(client):
    customer = create_customer_fixture()
    response = client.post("/api/token/", 
                         {
                            "email": "testuser@gmail.com", 
                            "password": "TestPassword123"
                         }, format="json")
    return response.json()["access"]
 
def create_customer_bid_fixture_with_access_token(client):
    access_token = create_jwt_hook(client)
    match = create_match_fixture()
    bid = Bid.objects.create(match=match, course="1.0v5.0")
    customer = Customer.objects.get(pk=1)
    customer_bid = CustomerBid.objects.create(customer=customer, 
                                              bid=bid, 
                                              winner=1,
                                              money_amount=30.0)
    return customer_bid, access_token