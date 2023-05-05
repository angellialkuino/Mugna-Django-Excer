# Generated by Django 4.2 on 2023-05-05 01:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("exercises", "0003_alter_author_email_alter_book_classification_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="author",
            name="user",
            field=models.OneToOneField(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
