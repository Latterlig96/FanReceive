from datetime import datetime
from django.test import TestCase
from matches.forms import MatchForm


class TestMatch(TestCase):

    def setUp(self):
        self.correct_case = {
            "title": "Test User vs Test User",
            "match_type": "Ekstraklasa",
            "match_result": "1:2",
            "match_schedule": datetime.now(),
            "description": "Test"   
        }
    
    def test_match_form_create(self):
        match = MatchForm(data=self.correct_case)
        assert match.is_valid()
    
    def test_match_form_fail_without_title(self):
        self.correct_case.pop("title")
        match = MatchForm(data=self.correct_case)
        assert not match.is_valid()
    
    def test_match_form_fail_with_empty_title(self):
        self.correct_case.update({"title": ""})
        match = MatchForm(data=self.correct_case)
        assert not match.is_valid()
    
    def test_match_form_fail_without_match_type(self):
        self.correct_case.pop("match_type")
        match = MatchForm(data=self.correct_case)
        assert not match.is_valid()
    
    def test_match_form_fail_with_empty_match_type(self):
        self.correct_case.update({"match_type": ""})
        match = MatchForm(data=self.correct_case)
        assert not match.is_valid()
    
    def test_match_form_fail_with_match_type_with_invalid_choice(self):
        self.correct_case.update({"match_type": "Test"})
        match = MatchForm(data=self.correct_case)
        error_message = ["Select a valid choice. Test is not one of the available choices."]
        self.assertEquals(match.errors.get("match_type"), error_message)
        assert not match.is_valid()
    
    def test_match_form_fail_without_match_result(self):
        self.correct_case.pop("match_result")
        match = MatchForm(data=self.correct_case)
        assert not match.is_valid()
    
    def test_match_form_fail_with_empty_match_result(self):
        self.correct_case.update({"match_result": ""})
        match = MatchForm(data=self.correct_case)
        assert not match.is_valid()
    
    def test_match_form_fail_with_failing_regex_for_match_result(self):
        self.correct_case.update({"match_result": "1v3"})
        match = MatchForm(data=self.correct_case)
        assert not match.is_valid()
    
    def test_match_form_fail_without_match_schedule(self):
        self.correct_case.pop("match_schedule")
        match = MatchForm(data=self.correct_case)
        assert not match.is_valid()
    
    def test_match_form_fail_with_empty_match_schedule(self):
        self.correct_case.update({"match_schedule": ""})
        match = MatchForm(data=self.correct_case)
        assert not match.is_valid()
