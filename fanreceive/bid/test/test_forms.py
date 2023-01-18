from bid.test.testconf import create_bid_fixture
from django.test import TestCase
from bid.forms import BidForm
 

class TestBid(TestCase):

    def setUp(self):
        self.bid_correct_case = create_bid_fixture()

    def test_bid_create(self):
        bid = BidForm(data=self.bid_correct_case)
        assert bid.is_valid()

    def test_fail_bid_create_without_match(self):
        self.bid_correct_case.pop("match")
        bid = BidForm(data=self.bid_correct_case)
        assert not bid.is_valid()
    
    def test_fail_bid_create_with_empty_match(self):
        self.bid_correct_case.update({"match": ""})
        bid = BidForm(data=self.bid_correct_case)
        assert not bid.is_valid()
    
    def test_fail_bid_create_without_course(self):
        self.bid_correct_case.pop("course")
        bid = BidForm(data=self.bid_correct_case)
        assert not bid.is_valid()
    
    def test_fail_bid_create_with_empty_course(self):
        self.bid_correct_case.update({"course": ""})
        bid = BidForm(data=self.bid_correct_case)
        assert not bid.is_valid()
    
    def test_fail_bid_create_with_invalid_course_regex(self):
        self.bid_correct_case.update({"course": "1.0:20.0"})
        bid = BidForm(data=self.bid_correct_case)
        assert not bid.is_valid()
