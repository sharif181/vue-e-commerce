# Generated by Django 3.2.11 on 2022-02-03 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0085_auto_20220128_1717'),
    ]

    operations = [
        migrations.AddField(
            model_name='request',
            name='zip_code',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='requesthistory',
            name='zip_code',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
