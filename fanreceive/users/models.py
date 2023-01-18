from django.db import models

from django.db import models
from django.core.validators import EmailValidator, MinValueValidator, MinLengthValidator
from django.contrib.auth.models import AbstractUser


class Customer(AbstractUser):

    _EMAIL_INCORRECT_MESSAGE = "Provided email is not correct"
    
    EMAIL_FIELD = "email"
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username",
                       "first_name", 
                       "last_name", 
                       "age", 
                       "password"]

    first_name = models.CharField(max_length=100, 
                                  blank=False, 
                                  null=False)
    last_name = models.CharField(max_length=100, 
                                 blank=False, 
                                 null=False)
    email = models.EmailField(max_length=100, 
                              unique=True, 
                              db_index=True, 
                              validators=[EmailValidator(message=_EMAIL_INCORRECT_MESSAGE)])
    age = models.PositiveIntegerField(null=False, 
                                      blank=False, 
                                      validators=[MinValueValidator(limit_value=18)])
    city = models.CharField(max_length=100, 
                            blank=True, 
                            null=True)
    password = models.CharField(max_length=100, 
                                validators=[MinLengthValidator(limit_value=10)])
    date_joined = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Customer %s %s" %(self.first_name, self.last_name)


class Activities(models.Model):

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    description = models.CharField(max_length=100, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Activities for: %s" %(self.customer)
