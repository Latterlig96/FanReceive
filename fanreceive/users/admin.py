from django.contrib import admin
from users.models import Customer

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    fields = "__all__"
    list_display = (
        "username",
        "first_name",
        "last_name",
        "email",
        "age",
        "city",
        "is_staff",
        "date_joined"
    )
    list_filter = ("date_joined",)
    fields = (
        "username",
        "first_name",
        "last_name",
        "email",
        "age",
        "city",
        "is_staff",
        "date_joined"
    )
