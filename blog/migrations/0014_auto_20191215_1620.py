# Generated by Django 3.0 on 2019-12-15 16:20

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_auto_20191215_1619'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categorie',
            name='utimestamp',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 15, 16, 20, 14, 660603, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 15, 16, 20, 14, 657811, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='tag',
            name='utimestamp',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 15, 16, 20, 14, 663436, tzinfo=utc)),
        ),
    ]