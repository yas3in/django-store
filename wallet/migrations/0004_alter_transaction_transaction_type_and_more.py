# Generated by Django 4.2 on 2024-10-16 18:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0003_alter_transaction_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='transaction_type',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Charge'), (2, 'Purchase'), (3, 'Transfer received'), (4, 'Transfer Sent')]),
        ),
        migrations.CreateModel(
            name='TransferTransaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('receiver_transaction', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='received_transaction', to='wallet.transaction')),
                ('sender_transaction', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='sender_transaction', to='wallet.transaction')),
            ],
        ),
    ]
