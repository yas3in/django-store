# Generated by Django 5.1 on 2024-09-08 17:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post_is_active_alter_post_last_name'),
        ('wallet', '0002_userbalance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='transactions', to='blog.user'),
        ),
    ]
