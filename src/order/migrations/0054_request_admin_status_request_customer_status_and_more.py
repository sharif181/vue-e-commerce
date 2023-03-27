# Generated by Django 4.0 on 2022-01-14 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0053_auto_20220112_2009'),
    ]

    operations = [
        migrations.AddField(
            model_name='request',
            name='admin_status',
            field=models.CharField(choices=[('pending', 'Pending'), ('in_review', 'In Review'), ('supplier_sent_review', 'Supplier Sent Review'), ('sent_review_to_customer', 'Sent Review to Customer'), ('submitted', 'Submitted'), ('cancelled', 'Cancelled')], default='pending', max_length=50),
        ),
        migrations.AddField(
            model_name='request',
            name='customer_status',
            field=models.CharField(choices=[('pending', 'Pending'), ('in_review', 'In Review'), ('supplier_sent_review', 'Supplier Sent Review'), ('sent_review_to_customer', 'Sent Review to Customer'), ('submitted', 'Submitted'), ('cancelled', 'Cancelled')], default='pending', max_length=50),
        ),
        migrations.AddField(
            model_name='request',
            name='supploer_status',
            field=models.CharField(choices=[('pending', 'Pending'), ('in_review', 'In Review'), ('supplier_sent_review', 'Supplier Sent Review'), ('sent_review_to_customer', 'Sent Review to Customer'), ('submitted', 'Submitted'), ('cancelled', 'Cancelled')], default='pending', max_length=50),
        ),
        migrations.AddField(
            model_name='requesthistory',
            name='admin_status',
            field=models.CharField(choices=[('pending', 'Pending'), ('in_review', 'In Review'), ('supplier_sent_review', 'Supplier Sent Review'), ('sent_review_to_customer', 'Sent Review to Customer'), ('submitted', 'Submitted'), ('cancelled', 'Cancelled')], default='pending', max_length=50),
        ),
        migrations.AddField(
            model_name='requesthistory',
            name='customer_status',
            field=models.CharField(choices=[('pending', 'Pending'), ('in_review', 'In Review'), ('supplier_sent_review', 'Supplier Sent Review'), ('sent_review_to_customer', 'Sent Review to Customer'), ('submitted', 'Submitted'), ('cancelled', 'Cancelled')], default='pending', max_length=50),
        ),
        migrations.AddField(
            model_name='requesthistory',
            name='supploer_status',
            field=models.CharField(choices=[('pending', 'Pending'), ('in_review', 'In Review'), ('supplier_sent_review', 'Supplier Sent Review'), ('sent_review_to_customer', 'Sent Review to Customer'), ('submitted', 'Submitted'), ('cancelled', 'Cancelled')], default='pending', max_length=50),
        ),
        migrations.AlterField(
            model_name='request',
            name='status',
            field=models.CharField(choices=[('pending', 'Pending'), ('in_review', 'In Review'), ('supplier_sent_review', 'Supplier Sent Review'), ('sent_review_to_customer', 'Sent Review to Customer'), ('submitted', 'Submitted'), ('cancelled', 'Cancelled')], default='pending', max_length=50),
        ),
        migrations.AlterField(
            model_name='requesthistory',
            name='status',
            field=models.CharField(choices=[('pending', 'Pending'), ('in_review', 'In Review'), ('supplier_sent_review', 'Supplier Sent Review'), ('sent_review_to_customer', 'Sent Review to Customer'), ('submitted', 'Submitted'), ('cancelled', 'Cancelled')], default='pending', max_length=50),
        ),
    ]