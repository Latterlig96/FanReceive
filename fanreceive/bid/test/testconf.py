import datetime
from matches.models import Match
from users.models import Customer
from bid.models import Bid
from decimal import Decimal


def create_bid_fixture():
    match_correct_case = {
        "title": "Test User vs Test User",
        "match_type": "Ekstraklasa",
        "match_result": "1:2",
        "match_schedule": datetime.date.today(),
        "description": "Test"   
        }
    match = Match.objects.create(**match_correct_case)
    return {
        "match": match,
        "course": "1.0v5.0"
    }

def create_customer_bid_fixture():
    user_correct_case = {
        "first_name": "TestName",
        "last_name": "TestSurname",
        "username": "TestUsername",
        "email": "testuser@gmail.com",
        "age": 20,
        "city": "Cracow",
        "password": "TestPassword123"
        }
    customer = Customer.objects.create(**user_correct_case)
    bid = Bid.objects.create(**create_bid_fixture())

    return {
        "customer": customer,
        "bid": bid,
        "winner": "1",
        "money_amount": Decimal(30.0)
    }
