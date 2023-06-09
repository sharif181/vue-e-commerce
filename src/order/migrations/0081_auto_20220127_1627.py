# Generated by Django 3.2.11 on 2022-01-27 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0080_auto_20220126_1930'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderinfo',
            name='admin_status',
            field=models.CharField(choices=[('received', 'Received'), ('processing', 'Processing'), ('processed', 'Processed'), ('shipped', 'Shipped'), ('delivered', 'Delivered'), ('returned', 'Returned'), ('canceled', 'Canceled')], max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='orderinfohistory',
            name='admin_status',
            field=models.CharField(choices=[('received', 'Received'), ('processing', 'Processing'), ('processed', 'Processed'), ('shipped', 'Shipped'), ('delivered', 'Delivered'), ('returned', 'Returned'), ('canceled', 'Canceled')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='orderinfo',
            name='status',
            field=models.CharField(blank=True, choices=[('received', 'Received'), ('processing', 'Processing'), ('processed', 'Processed'), ('shipped', 'Shipped'), ('delivered', 'Delivered'), ('returned', 'Returned'), ('canceled', 'Canceled')], max_length=50),
        ),
        migrations.AlterField(
            model_name='orderinfohistory',
            name='status',
            field=models.CharField(blank=True, choices=[('received', 'Received'), ('processing', 'Processing'), ('processed', 'Processed'), ('shipped', 'Shipped'), ('delivered', 'Delivered'), ('returned', 'Returned'), ('canceled', 'Canceled')], max_length=50),
        ),
    ]
