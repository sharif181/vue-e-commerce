# Generated by Django 4.0 on 2021-12-24 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0028_remove_selectedrequestreview_review_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='request',
            name='modified_number',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='requesthistory',
            name='modified_number',
            field=models.IntegerField(default=0),
        ),
    ]