# Generated by Django 3.2.9 on 2021-11-22 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('utils', '0001_initial'),
        ('product', '0004_auto_20211122_1036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attribute',
            name='unit',
            field=models.ManyToManyField(blank=True, null=True, to='utils.Unit'),
        ),
    ]