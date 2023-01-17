from users.models import Customer
from users.models import Activities
from django.db.models.signals import post_save
from django.dispatch import receiver


@receiver(post_save, sender=Customer)
def create_activity_for_customer(sender: Customer, 
                                 instance: Customer, 
                                 created: bool, 
                                 **kwargs):
    if created: 
        description = "Created account for %s %s" %(instance.first_name, instance.last_name)
        Activities.objects.create(customer=instance,
                                  description=description)
