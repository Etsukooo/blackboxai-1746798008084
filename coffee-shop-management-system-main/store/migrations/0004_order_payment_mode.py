# Generated by Django 5.2 on 2025-05-07 22:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_cart_cartitem'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='payment_mode',
            field=models.CharField(choices=[('COD', 'Cash on Delivery'), ('GCASH', 'GCASH'), ('DEBIT', 'Debit Card'), ('CREDIT_CARD', 'Credit Card')], default='COD', max_length=20),
        ),
    ]
