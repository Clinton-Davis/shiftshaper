from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from users.models import UserProfile


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """Create or update user profile from signals."""

    if created:
        UserProfile.objects.create(user=instance)
    else:
        # Ensure we access the profile using the correct related_name
        profile, created = UserProfile.objects.get_or_create(user=instance)
        if not created:
            profile.save()
