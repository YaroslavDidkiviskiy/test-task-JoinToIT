from rest_framework import serializers
from .models import Registration
from apps.events.serializers import EventSerializer


class RegistrationSerializer(serializers.ModelSerializer):
    event_detail = EventSerializer(source="event", read_only=True)

    class Meta:
        model = Registration
        fields = ["id", "event", "event_detail", "registered_at"]
        read_only_fields = ["id", "registered_at"]

    def validate(self, attrs):
        user = self.context["request"].user
        event = attrs["event"]
        if Registration.objects.filter(user=user, event=event).exists():
            raise serializers.ValidationError("You are already registered for this event.")
        return attrs
