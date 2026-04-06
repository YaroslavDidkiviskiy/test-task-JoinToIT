from django.contrib import admin
from .models import Registration


@admin.register(Registration)
class RegistrationAdmin(admin.ModelAdmin):
    list_display = ["user", "event", "registered_at"]
    list_filter = ["event"]
    search_fields = ["user__email", "event__title"]
