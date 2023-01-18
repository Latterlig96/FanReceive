from django.db import models

from decimal import Decimal
from matches.models import Match
from users.models import Customer
from django.core.validators import RegexValidator


class Bid(models.Model):

    match = models.ForeignKey(Match, on_delete=models.DO_NOTHING)
    course = models.CharField(max_length=20, 
                              blank=False, 
                              null=False,
                              validators=[RegexValidator(regex="\d\.\dv\d\.\d")])
    
    def __str__(self):
        return "Bid for match: %s" %(self.match)


class CustomerBid(models.Model):

    _BID_CHOICES = (
        (0, "First team will win"),
        (1, "Second team will win")
    )

    customer = models.ForeignKey(Customer, on_delete=models.DO_NOTHING)
    bid = models.ForeignKey(Bid, on_delete=models.DO_NOTHING)
    winner = models.IntegerField(blank=False, 
                                 null=False,
                                 choices=_BID_CHOICES)
    money_amount = models.DecimalField(max_digits=100, 
                                       decimal_places=2, 
                                       null=False,
                                       blank=False)
    
    def calculate_money_obtained_from_bid(self):
        bid_match = self.bid.match
        if bid_match.match_result == "Pending":
            return 0
        match_result = [int(result) for result in bid_match.match_result.split(":")]
        course = [Decimal(float(course)) for course in self.bid.course.split("v")]
        match_result = 0 if match_result[0] > match_result[1] else 1
        if match_result == int(self.winner):
            return course[match_result] * self.money_amount
        return 0 

    def __str__(self):
        return "Bid for customer: %s" %(self.customer)
