# Generated by Django 3.2.9 on 2021-11-22 10:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('utils', '0001_initial'),
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='classification',
            name='is_optional',
        ),
        migrations.AlterField(
            model_name='attribute',
            name='unit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='utils.unit'),
        ),
        migrations.AlterField(
            model_name='classification',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
