# Generated by Django 3.2.9 on 2021-12-14 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0006_alter_order_created_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('pending', 'pending'), ('in review', 'in review'), ('accepted', 'accepted'), ('completed', 'completed')], default='pending', max_length=50),
        ),
    ]
