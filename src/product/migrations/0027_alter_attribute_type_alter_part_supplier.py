# Generated by Django 4.0 on 2021-12-15 06:05

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('product', '0026_merge_20211214_1350'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attribute',
            name='type',
            field=models.CharField(choices=[('text', 'Text'), ('number', 'Number'), ('select', 'Select')], default='text', max_length=255),
        ),
        migrations.AlterField(
            model_name='part',
            name='supplier',
            field=models.ManyToManyField(blank=True, null=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
