# Generated by Django 3.2.11 on 2022-01-27 12:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0082_auto_20220127_1813'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderinfo',
            name='admin_status',
        ),
        migrations.RemoveField(
            model_name='orderinfohistory',
            name='admin_status',
        ),
    ]
