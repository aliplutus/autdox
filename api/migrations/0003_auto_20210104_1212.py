# Generated by Django 3.1.4 on 2021-01-04 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_book_who_can_see'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='who_can_see',
            field=models.ManyToManyField(blank=True, related_name='tweet_user', to='api.Author'),
        ),
    ]
