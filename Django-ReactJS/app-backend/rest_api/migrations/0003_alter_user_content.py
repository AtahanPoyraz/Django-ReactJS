# Generated by Django 4.2.3 on 2023-08-06 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest_api', '0002_alter_user_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='content',
            field=models.TextField(blank=True, default='', verbose_name='content'),
        ),
    ]
