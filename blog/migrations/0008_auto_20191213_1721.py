# Generated by Django 3.0 on 2019-12-13 17:21

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20191213_1552'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categories',
            name='utimestamp',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 13, 17, 21, 7, 279712, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 13, 17, 21, 7, 278599, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='tag',
            name='utimestamp',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 13, 17, 21, 7, 281321, tzinfo=utc)),
        ),
    ]