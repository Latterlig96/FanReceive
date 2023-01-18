import datetime
from django.test import TestCase
from users.forms import CustomerForm


class TestCustomer(TestCase):

    def setUp(self):
        self.correct_case = {
            "first_name": "TestName",
            "last_name": "TestSurname",
            "username": "TestUsername",
            "email": "testuser@gmail.com",
            "age": 20,
            "city": "Cracow",
            "password": "TestPassword123",
            "date_joined": datetime.datetime.now()
        }
    
    def test_customer_form_create(self):
        customer = CustomerForm(data=self.correct_case)
        print(customer.errors)
        assert customer.is_valid()
    
    def test_fail_customer_form_without_username(self):
        self.correct_case.pop("username")
        customer = CustomerForm(data=self.correct_case)
        assert not customer.is_valid()
    
    def test_fail_customer_form_with_empty_username(self):
        self.correct_case.update({"username": ""})
        customer = CustomerForm(data=self.correct_case)
        assert not customer.is_valid()
    
    def test_fail_customer_form_without_first_name(self):
        self.correct_case.pop("first_name")
        customer = CustomerForm(data=self.correct_case)
        assert not customer.is_valid()
    
    def test_fail_customer_form_with_empty_first_name(self):
        self.correct_case.update({"first_name": ""})
        customer = CustomerForm(data=self.correct_case)
        assert not customer.is_valid()
    
    def test_fail_customer_form_without_last_name(self):
        self.correct_case.pop("last_name")
        customer = CustomerForm(data=self.correct_case)
        assert not customer.is_valid()
    
    def test_fail_customer_form_with_empty_last_name(self):
        self.correct_case.update({"last_name": ""})
        customer = CustomerForm(data=self.correct_case)
        assert not customer.is_valid()
    
    def test_fail_customer_form_without_email(self):
        self.correct_case.pop("email")
        customer = CustomerForm(data=self.correct_case)
        assert not customer.is_valid()
    
    def test_fail_customer_form_with_empty_email(self):
        self.correct_case.update({"email": ""})
        customer = CustomerForm(data=self.correct_case)
        assert not customer.is_valid()
    
    def test_fail_customer_form_with_empty_invalid_email(self):
        self.correct_case.update({"email": "testemailnotgood"})
        customer = CustomerForm(data=self.correct_case)
        assert not customer.is_valid()
    
    def test_fail_customer_form_without_age(self):
        self.correct_case.pop("age")
        customer = CustomerForm(data=self.correct_case)
        assert not customer.is_valid()
    
    def test_fail_customer_form_with_empty_age(self):
        self.correct_case.update({"age": ""})
        customer = CustomerForm(data=self.correct_case)
        assert not customer.is_valid()
    
    def test_fail_customer_form_with_age_less_than_threshold(self):
        self.correct_case.update({"age": 16})
        error_message = ["Ensure this value is greater than or equal to 18."]
        customer = CustomerForm(data=self.correct_case)
        self.assertEquals(customer.errors.get("age"), error_message)
        assert not customer.is_valid()
    
    def test_fail_customer_form_without_password(self):
        self.correct_case.pop("password")
        customer = CustomerForm(data=self.correct_case)
        assert not customer.is_valid()
    
    def test_fail_customer_form_with_empty_password(self):
        self.correct_case.update({"password": ""})
        customer = CustomerForm(data=self.correct_case)
        assert not customer.is_valid()
    
    def test_fail_customer_form_with_too_short_password(self):
        self.correct_case.update({"password": "test"})
        error_message = ["Ensure this value has at least 10 characters (it has 4)."]
        customer = CustomerForm(data=self.correct_case)
        self.assertEquals(customer.errors.get("password"), error_message)
        assert not customer.is_valid()
