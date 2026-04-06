from rest_framework import serializers
from .models import Event


class EventSerializer(serializers.ModelSerializer):
    organizer = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Event
        fields = ["id", "title", "description", "date", "location", "organizer", "created_at", "updated_at"]
        read_only_fields = ["id", "organizer", "created_at", "updated_at"]
