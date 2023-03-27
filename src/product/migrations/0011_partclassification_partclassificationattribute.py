# Generated by Django 3.2.9 on 2021-11-24 12:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_userforeignkey.models.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('product', '0010_auto_20211124_1222'),
    ]

    operations = [
        migrations.CreateModel(
            name='PartClassification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_required', models.CharField(blank=True, max_length=255, null=True)),
                ('classification', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.classification')),
                ('created_by', django_userforeignkey.models.fields.UserForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='product_partclassification_related', to=settings.AUTH_USER_MODEL, verbose_name='Created By')),
                ('part', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.part')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PartClassificationAttribute',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('attribute', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.attribute')),
                ('created_by', django_userforeignkey.models.fields.UserForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='product_partclassificationattribute_related', to=settings.AUTH_USER_MODEL, verbose_name='Created By')),
                ('part_classification', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.partclassification')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
