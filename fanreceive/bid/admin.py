from django.contrib import admin

from bid.models import Bid, CustomerBid


@admin.register(Bid)
class BidAdmin(admin.ModelAdmin):
    list_display = ("match", "course")

@admin.register(CustomerBid)
class CustomerBidAdmin(admin.ModelAdmin):
    list_display = ("customer", "bid", "winner", "money_amount")
