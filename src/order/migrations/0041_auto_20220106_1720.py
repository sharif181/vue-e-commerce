# Generated by Django 3.2.10 on 2022-01-06 11:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0040_auto_20220106_1654'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderinfo',
            name='request',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='order.request'),
        ),
        migrations.AlterField(
            model_name='orderinfohistory',
            name='request',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='order.request'),
        ),
    ]
