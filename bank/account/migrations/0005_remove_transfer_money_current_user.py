# Generated by Django 3.0.5 on 2020-04-13 11:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_auto_20200413_1722'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transfer_money',
            name='current_user',
        ),
    ]
