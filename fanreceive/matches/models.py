from datetime import date

from django.db import models

from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator


class Match(models.Model):

    _MATCH_TYPE_CHOICES = (
        ("Premier League", "PL"),
        ("Champions League", "CL"),
        ("Ekstraklasa", "EK"),
        ("NFL", "NFL"),
        ("NBA", "NBA")
    )

    title = models.CharField(max_length=100, 
                             blank=False, 
                             null=False)
    match_type = models.CharField(max_length=50, choices=_MATCH_TYPE_CHOICES)
    match_result = models.CharField(max_length=10, 
                                    default="Pending", 
                                    blank=False, 
                                    null=False,
                                    validators=[RegexValidator(regex="(\d\:\d)|(Pending)")])
    match_schedule = models.DateTimeField(blank=False, 
                                          null=False)
    description = models.TextField()
    image = models.ImageField(upload_to="matches/", 
                              blank=True, 
                              null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Match: %s" %(self.title)

    def save(self, *args, **kwargs):
        if self.match_schedule.date() < date.today():
            raise ValidationError("Match schedule cannot be less than today's date")
        return super().save(*args, **kwargs)
