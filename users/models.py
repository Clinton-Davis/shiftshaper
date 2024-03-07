from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class UserProfile(models.Model):
    ROLE_CHOICES = [
        ("admin", "Admin"),
        ("manager", "Manager"),
        ("staff", "Staff"),
    ]

    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="user_profile"
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default="staff")
    phone = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return f"{self.user.username}'s profile"
