# Generated by Django 4.1 on 2022-09-15 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("enrolment", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="status",
            field=models.CharField(default="student", max_length=64),
            preserve_default=False,
        ),
    ]
