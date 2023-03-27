# Generated by Django 3.2.10 on 2022-01-19 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0062_auto_20220119_1839'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requestreview',
            name='lead_time',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='requestreview',
            name='quantity',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='requestreview',
            name='supplier_cost',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='requestreview',
            name='supplier_lead_time',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
    ]
