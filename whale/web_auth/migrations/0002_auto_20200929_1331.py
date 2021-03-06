# Generated by Django 3.0.8 on 2020-09-29 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_auth', '0001_initial'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='otpdevice',
            name='otp_device_name_unique',
        ),
        migrations.RenameField(
            model_name='otpdevice',
            old_name='user_id',
            new_name='user',
        ),
        migrations.AddConstraint(
            model_name='otpdevice',
            constraint=models.UniqueConstraint(fields=('user', 'name'), name='otp_device_name_unique'),
        ),
    ]
