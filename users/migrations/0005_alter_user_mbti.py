# Generated by Django 4.1.2 on 2022-11-02 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0004_alter_user_email_alter_user_nickname"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="mbti",
            field=models.CharField(blank=True, max_length=4),
        ),
    ]
