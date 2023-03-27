# Generated by Django 4.0 on 2021-12-20 11:24

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0020_alter_requestreview_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='requestreview',
            old_name='order',
            new_name='request',
        ),
        migrations.AlterField(
            model_name='requestreview',
            name='attachment',
            field=models.FileField(help_text='Allow PDF file only', upload_to='', validators=[django.core.validators.FileExtensionValidator(['pdf'])]),
        ),
    ]