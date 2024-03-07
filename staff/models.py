from django.db import models
from django.contrib.auth.models import User


class StaffProfile(models.Model):
    DAY_CHOICES = [
        ("monday", "Monday"),
        ("tuesday", "Tuesday"),
        ("wednesday", "Wednesday"),
        ("thursday", "Thursday"),
        ("friday", "Friday"),
        ("saturday", "Saturday"),
        ("sunday", "Sunday"),
        ("none", "None"),
    ]
    user_profile = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="staff_profile"
    )
    max_shifts_per_week = models.PositiveIntegerField(default=5)

    unavailable_days = models.CharField(
        max_length=20, choices=DAY_CHOICES, default="none"
    )

    def __str__(self):
        return f"{self.user_profile.user.username}'s Staff Profile"


class TimeOffRequest(models.Model):
    staff_profile = models.ForeignKey(
        StaffProfile, on_delete=models.CASCADE, related_name="time_off_requests"
    )
    start_date = models.DateField()
    end_date = models.DateField()
    is_approved = models.BooleanField(default=False)
    request_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.staff_profile.user_profile.username} - from {self.start_date} to {self.end_date} - {'Approved' if self.is_approved else 'Pending'}"

    class Meta:
        ordering = ["start_date"]

    @property
    def is_single_day(self):
        return self.start_date == self.end_date
