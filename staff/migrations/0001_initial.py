# Generated by Django 5.0.3 on 2024-03-07 19:42

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='StaffProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('max_shifts_per_week', models.PositiveIntegerField(default=5)),
                ('unavailable_days', models.CharField(choices=[('monday', 'Monday'), ('tuesday', 'Tuesday'), ('wednesday', 'Wednesday'), ('thursday', 'Thursday'), ('friday', 'Friday'), ('saturday', 'Saturday'), ('sunday', 'Sunday'), ('none', 'None')], default='none', max_length=20)),
                ('user_profile', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='staff_profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TimeOffRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('is_approved', models.BooleanField(default=False)),
                ('request_created', models.DateTimeField(auto_now_add=True)),
                ('staff_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='time_off_requests', to='staff.staffprofile')),
            ],
            options={
                'ordering': ['start_date'],
            },
        ),
    ]