import datetime
from django.test import TestCase
from matches.models import Match
from django.db.utils import IntegrityError
from django.core.exceptions import ValidationError


class TestMatch(TestCase):

    def setUp(self):
        self.correct_case = {
            "title": "Test User vs Test User",
            "match_type": "Ekstraklasa",
            "match_result": "1:2",
            "match_schedule": datetime.datetime.now(),
            "description": "Test"   
        }
    
    def test_match_create(self):
        match = Match.objects.create(**self.correct_case)
        assert Match.objects.count() == 1
        assert Match.objects.filter(pk=match.pk).exists()
    
    def test_match_create_fail_because_empty_title(self):
        self.correct_case.update({"title": None})
        with self.assertRaises(IntegrityError):
            Match.objects.create(**self.correct_case)
            assert Match.objects.count() == 0
    
    def test_match_create_fail_because_empty_match_type(self):
        self.correct_case.update({"match_type": None})
        with self.assertRaises(IntegrityError):
            Match.objects.create(**self.correct_case)
            assert Match.objects.count() == 0
    
    def test_match_create_fail_because_empty_match_result(self):
        self.correct_case.update({"match_result": None})
        with self.assertRaises(IntegrityError):
            Match.objects.create(**self.correct_case)
            assert Match.objects.count() == 0
    
    def test_match_create_fail_because_match_schedule_is_in_past(self):
        self.correct_case.update({"match_schedule": datetime.datetime.now() - datetime.timedelta(days=1)})
        with self.assertRaises(ValidationError):
            Match.objects.create(**self.correct_case)
            assert Match.objects.count() == 0
