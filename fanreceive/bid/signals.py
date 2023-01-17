from bid.models import CustomerBid
from users.models import Activities
from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=CustomerBid)
def create_bid_activity_for_customer(sender: CustomerBid, 
                                     instance: CustomerBid,
                                     created: bool,
                                     **kwargs):
    if created:
        description = "Created bid for %s" %(instance.bid.match)
        Activities.objects.create(customer=instance.customer,
                                  description=description)
