from django.apps import AppConfig


class BidConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "bid"

    def ready(self):
        from bid.signals import create_bid_activity_for_customer
