# Generated by Django 4.2.5 on 2023-12-20 19:09

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("countries", "0003_alter_uservisitedcountry_date_visited"),
    ]

    operations = [
        migrations.AlterField(
            model_name="uservisitedcountry",
            name="date_visited",
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]