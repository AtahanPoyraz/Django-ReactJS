# Generated by Django 4.2.3 on 2023-08-07 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest_api', '0004_user_time_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='token',
            field=models.CharField(blank=True, default=True, max_length=255),
        ),
    ]
