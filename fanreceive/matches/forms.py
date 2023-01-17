from django import forms

from matches.models import Match


class MatchForm(forms.ModelForm):
    class Meta:
        model = Match
        fields = "__all__"
