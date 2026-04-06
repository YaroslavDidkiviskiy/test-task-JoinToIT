from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings


@shared_task
def send_registration_email(user_email, event_title, event_date, event_location):
    send_mail(
        subject=f"Registration confirmed: {event_title}",
        message=(
            f"Hi!\n\n"
            f"You have successfully registered for the event:\n\n"
            f"📅 {event_title}\n"
            f"📍 Location: {event_location}\n"
            f"🕐 Date: {event_date}\n\n"
            f"See you there!"
        ),
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[user_email],
        fail_silently=False,
    )
