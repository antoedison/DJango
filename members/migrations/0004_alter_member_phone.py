# Generated by Django 5.1.5 on 2025-02-09 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0003_member_joined_date_member_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='phone',
            field=models.BigIntegerField(null=True),
        ),
    ]
