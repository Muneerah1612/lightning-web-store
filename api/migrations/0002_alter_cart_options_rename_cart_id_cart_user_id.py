# Generated by Django 4.0.5 on 2022-06-29 01:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="cart",
            options={"ordering": ["user_id", "-created_at"]},
        ),
        migrations.RenameField(
            model_name="cart",
            old_name="cart_id",
            new_name="user_id",
        ),
    ]
