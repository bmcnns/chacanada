# Generated by Django 2.2.3 on 2019-08-05 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chac', '0013_remove_user_cart'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='cart',
            field=models.CharField(default='null', max_length=1500),
            preserve_default=False,
        ),
    ]
