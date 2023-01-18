from django import forms
from bid.models import Bid


class BidForm(forms.ModelForm):
    class Meta:
        model = Bid
        fields = "__all__"
