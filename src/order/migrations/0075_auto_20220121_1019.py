# Generated by Django 3.2.9 on 2022-01-21 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0074_auto_20220121_0940'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderinfo',
            name='status',
            field=models.CharField(choices=[('pending', 'Pending'), ('in_review', 'In Review'), ('accepted', 'Accepted'), ('completed', 'Completed'), ('cancel', 'Cancel')], default='pending', max_length=50),
        ),
        migrations.AlterField(
            model_name='orderinfohistory',
            name='status',
            field=models.CharField(choices=[('pending', 'Pending'), ('in_review', 'In Review'), ('accepted', 'Accepted'), ('completed', 'Completed'), ('cancel', 'Cancel')], default='pending', max_length=50),
        ),
    ]
