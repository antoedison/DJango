# Generated by Django 5.1.5 on 2025-02-01 04:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0002_remove_member_email_remove_member_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='joined_date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='member',
            name='phone',
            field=models.IntegerField(null=True),
        ),
    ]
