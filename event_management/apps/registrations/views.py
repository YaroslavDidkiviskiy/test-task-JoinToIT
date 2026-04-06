from rest_framework import viewsets, permissions, mixins

from .models import Registration
from .serializers import RegistrationSerializer
from .tasks import send_registration_email


class RegistrationViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):
    serializer_class = RegistrationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Registration.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        registration = serializer.save(user=self.request.user)
        send_registration_email.delay(
            user_email=self.request.user.email,
            event_title=registration.event.title,
            event_date=str(registration.event.date),
            event_location=registration.event.location,
        )
