# Generated by Django 2.2.3 on 2019-08-01 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chac', '0008_auto_20190801_1328'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='item_cost',
            field=models.FloatField(default=0),
        ),
    ]
