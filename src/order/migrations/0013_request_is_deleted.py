# Generated by Django 4.0 on 2021-12-17 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0012_requesthistory'),
    ]

    operations = [
        migrations.AddField(
            model_name='request',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
    ]
