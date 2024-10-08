# Generated by Django 5.1 on 2024-09-02 12:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalouge', '0010_alter_brand_parent_alter_category_parent'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productattributevalue',
            old_name='attriذute',
            new_name='attribute',
        ),
        migrations.AddField(
            model_name='product',
            name='brand',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='products', to='catalouge.brand'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='products', to='catalouge.category'),
            preserve_default=False,
        ),
    ]
