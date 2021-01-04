# Generated by Django 3.1.4 on 2021-01-04 14:41

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0005_auto_20210104_1428'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='who_can_see',
            field=models.ManyToManyField(blank=True, related_name='tweet_user', to=settings.AUTH_USER_MODEL),
        ),
    ]
