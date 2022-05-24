from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Profile
from user.enums import *


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_profile(sender, instance, created, **kwargs):
    print("Signal")
    if created:
        print("User created")
        if instance.is_superuser:
            Profile.objects.create(user=instance, role=UserRole.SuperAdmin)
        else:
            Profile.objects.create(user=instance, role=UserRole.Guest)


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def save_profile(sender, instance, **kwargs):
    print("User saved")
    instance.profile.save()
