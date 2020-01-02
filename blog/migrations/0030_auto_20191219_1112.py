# Generated by Django 3.0 on 2019-12-19 11:12

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0029_auto_20191219_1040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categorie',
            name='utimestamp',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 19, 11, 12, 30, 765198, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='comment',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 19, 11, 12, 30, 763715, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 19, 11, 12, 30, 759889, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='tag',
            name='utimestamp',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 19, 11, 12, 30, 766129, tzinfo=utc)),
        ),
    ]
