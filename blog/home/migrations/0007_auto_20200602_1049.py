# Generated by Django 2.1.8 on 2020-06-02 02:49

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_auto_20200602_1020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlecategory',
            name='created',
            field=models.DateField(default=datetime.datetime(2020, 6, 2, 2, 49, 23, 121122, tzinfo=utc)),
        ),
    ]
