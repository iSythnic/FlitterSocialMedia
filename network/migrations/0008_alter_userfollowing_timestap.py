# Generated by Django 4.0.6 on 2022-12-25 01:34

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0007_remove_user_followers_remove_user_following_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userfollowing',
            name='timestap',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 25, 1, 34, 0, 407599, tzinfo=utc)),
        ),
    ]
