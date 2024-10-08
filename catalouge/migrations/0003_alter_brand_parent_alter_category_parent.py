# Generated by Django 5.1 on 2024-09-02 10:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalouge', '0002_rename_brand_id_product_brand_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brand',
            name='parent',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, related_name='children', to='catalouge.brand'),
        ),
        migrations.AlterField(
            model_name='category',
            name='parent',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, related_name='children', to='catalouge.category'),
        ),
    ]
