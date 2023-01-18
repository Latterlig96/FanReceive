from django.test import TestCase
from users.models import Customer
from django.db.utils import IntegrityError
from django.db.models.signals import post_save
from unittest.mock import patch


class TestCustomer(TestCase):

    def setUp(self):
        self.correct_case = {
            "first_name": "TestName",
            "last_name": "TestSurname",
            "username": "TestUsername",
            "email": "testuser@gmail.com",
            "age": 20,
            "city": "Cracow",
            "password": "TestPassword123"
        }

    def test_customer_create(self):
        customer = Customer.objects.create(**self.correct_case)
        assert Customer.objects.count() == 1
        assert Customer.objects.filter(pk=customer.pk).exists()
    
    def test_fail_customer_create_without_first_name(self):
        self.correct_case.update({"first_name": None})
        with self.assertRaises(IntegrityError):
            Customer.objects.create(**self.correct_case)
            assert Customer.objects.count() == 0
    
    def test_fail_customer_create_without_last_name(self):
        self.correct_case.update({"last_name": None})
        with self.assertRaises(IntegrityError):
            Customer.objects.create(**self.correct_case)
            assert Customer.objects.count() == 0
        
    def test_fail_customer_create_without_username(self):
        self.correct_case.update({"username": None})
        with self.assertRaises(IntegrityError):
            Customer.objects.create(**self.correct_case)
            assert Customer.objects.count() == 0
    
    def test_fail_customer_create_without_email(self):
        self.correct_case.update({"email": None})
        with self.assertRaises(IntegrityError):
            Customer.objects.create(**self.correct_case)
            assert Customer.objects.count() == 0
    
    def test_fail_customer_create_without_age(self):
        self.correct_case.update({"age": None})
        with self.assertRaises(IntegrityError):
            Customer.objects.create(**self.correct_case)
            assert Customer.objects.count() == 0
    
    def test_fail_customer_create_without_password(self):
        self.correct_case.update({"password": None})
        with self.assertRaises(IntegrityError):
            Customer.objects.create(**self.correct_case)
            assert Customer.objects.count() == 0
    
    def test_activity_created_on_customer_creation(self):
        with patch("users.signals.create_activity_for_customer") as mock_signal:
            post_save.connect(mock_signal, sender=Customer, dispatch_uid="test_mock")
        Customer.objects.create(**self.correct_case)
        assert Customer.objects.count() == 1
        assert mock_signal.call_count == 1
    
    
