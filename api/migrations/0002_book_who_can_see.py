# Generated by Django 3.1.4 on 2021-01-04 10:58

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='who_can_see',
            field=models.ManyToManyField(blank=True, related_name='tweet_user', to=settings.AUTH_USER_MODEL),
        ),
    ]
