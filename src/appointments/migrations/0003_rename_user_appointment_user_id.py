# Generated by Django 5.0.9 on 2024-10-27 21:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0002_rename_member_appointment_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='appointment',
            old_name='user',
            new_name='user_id',
        ),
    ]