# Generated by Django 5.0.9 on 2024-10-27 21:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='appointment',
            old_name='member',
            new_name='user',
        ),
    ]
