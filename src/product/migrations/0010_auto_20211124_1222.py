# Generated by Django 3.2.9 on 2021-11-24 12:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0009_auto_20211122_1301'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='part',
            name='attribute',
        ),
        migrations.RemoveField(
            model_name='part',
            name='classification',
        ),
    ]
