# Generated by Django 3.2.9 on 2021-12-01 07:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0013_alter_partclassification_classification'),
    ]

    operations = [
        migrations.RenameField(
            model_name='partclassification',
            old_name='is_required',
            new_name='is_optional',
        ),
    ]