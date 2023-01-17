from django.contrib import admin
from matches.models import Match
from matches.forms import MatchForm


@admin.register(Match)
class MatchAdmin(admin.ModelAdmin):
    list_display = ("title", 
                    "match_type", 
                    "match_result", 
                    "match_schedule",
                    "description",
                    "image",
                    "created_at",
                    "updated_at"
                )
    fields = (
        "title",
        "match_type",
        "match_result",
        "match_schedule",
        "description",
        "image"
    )
    form = MatchForm
