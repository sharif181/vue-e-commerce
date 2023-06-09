# Generated by Django 4.0 on 2021-12-17 07:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_userforeignkey.models.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('product', '0029_remove_part_supplier_partsupplier'),
        ('authentication', '0006_delete_userrole'),
        ('order', '0011_delete_requesthistory'),
    ]

    operations = [
        migrations.CreateModel(
            name='RequestHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('answer', models.JSONField()),
                ('comment', models.CharField(blank=True, max_length=1000, null=True)),
                ('contact_info', models.JSONField()),
                ('quantity', models.FloatField()),
                ('type', models.CharField(choices=[('query', 'Query'), ('quote', 'Quote')], max_length=10)),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('in_review', 'In Review'), ('accepted', 'Accepted'), ('completed', 'Completed')], default='pending', max_length=50)),
                ('order_id', models.CharField(blank=True, max_length=255)),
                ('created_by', django_userforeignkey.models.fields.UserForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(app_label)s_%(class)s_related', to=settings.AUTH_USER_MODEL, verbose_name='Created By')),
                ('part', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='product.part')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='authentication.user')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
