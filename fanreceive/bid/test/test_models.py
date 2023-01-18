from bid.test.testconf import create_bid_fixture, create_customer_bid_fixture
from django.test import TestCase
from bid.models import Bid, CustomerBid
from matches.models import Match
from django.db.utils import IntegrityError


class TestBid(TestCase):

    def setUp(self):
        self.bid_correct_case = create_bid_fixture()
    
    def test_bid_create(self):
        bid = Bid.objects.create(**self.bid_correct_case)
        assert Bid.objects.count() == 1
        assert Bid.objects.filter(pk=bid.pk).exists()
    
    def test_bid_fail_create_without_match(self):
        self.bid_correct_case.update({"match": None})
        with self.assertRaises(IntegrityError):
            bid = Bid.objects.create(**self.bid_correct_case)
            assert Bid.objects.count() == 0
    
    def test_bid_fail_create_without_course(self):
        self.bid_correct_case.update({"course": None})
        with self.assertRaises(IntegrityError):
            bid = Bid.objects.create(**self.bid_correct_case)
            assert Bid.objects.count() == 0


class TestCustomerBid(TestCase):

    def setUp(self):
        self.customer_bid_correct_case = create_customer_bid_fixture()
    
    def test_customer_bid_create(self):
        customer_bid = CustomerBid.objects.create(**self.customer_bid_correct_case)
        assert CustomerBid.objects.count() == 1
        assert CustomerBid.objects.filter(pk=customer_bid.pk).exists()

    def test_customer_bid_fail_create_without_customer(self):
        self.customer_bid_correct_case.update({"customer": None})
        with self.assertRaises(IntegrityError):
            customer_bid = CustomerBid.objects.create(**self.customer_bid_correct_case)
            assert CustomerBid.objects.count() == 0
    
    def test_customer_bid_fail_create_without_bid(self):
        self.customer_bid_correct_case.update({"bid": None})
        with self.assertRaises(IntegrityError):
            customer_bid = CustomerBid.objects.create(**self.customer_bid_correct_case)
            assert CustomerBid.objects.count() == 0
    
    def test_customer_bid_fail_create_without_winner(self):
        self.customer_bid_correct_case.update({"winner": None})
        with self.assertRaises(IntegrityError):
            customer_bid = CustomerBid.objects.create(**self.customer_bid_correct_case)
            assert CustomerBid.objects.count() == 0
    
    def test_customer_bid_fail_create_without_money_amount(self):
        self.customer_bid_correct_case.update({"money_amount": None})
        with self.assertRaises(IntegrityError):
            customer_bid = CustomerBid.objects.create(**self.customer_bid_correct_case)
            assert CustomerBid.objects.count() == 0
    
    def test_customer_win_calulaction(self):
        customer_bid = CustomerBid.objects.create(**self.customer_bid_correct_case)
        expected_win_amount = 150
        match: Match = self.customer_bid_correct_case["bid"].match
        match.match_result = "0:1"
        match.save()
        win_amount = customer_bid.calculate_money_obtained_from_bid()
        assert win_amount == expected_win_amount
