# Generated by Django 3.2.9 on 2021-12-02 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0021_alter_partclassification_is_optional'),
    ]

    operations = [
        migrations.AddField(
            model_name='partclassificationattribute',
            name='is_optional',
            field=models.CharField(blank=True, default='False', max_length=50),
        ),
        migrations.AlterField(
            model_name='partclassification',
            name='is_optional',
            field=models.CharField(blank=True, default='False', max_length=255),
        ),
    ]