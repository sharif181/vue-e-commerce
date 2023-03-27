# Generated by Django 4.0 on 2021-12-28 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0031_rename_requstreviewattachments_requstreviewattachment'),
    ]

    operations = [
        migrations.AddField(
            model_name='request',
            name='cost',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='request',
            name='lead_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='requesthistory',
            name='cost',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='requesthistory',
            name='lead_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]