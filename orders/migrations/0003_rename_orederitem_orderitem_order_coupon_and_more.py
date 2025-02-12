# Generated by Django 5.1.4 on 2025-02-12 17:55

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coupons', '0001_initial'),
        ('orders', '0002_alter_order_options_alter_order_postal_code'),
        ('shop', '0002_alter_product_options_alter_category_name_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='OrederItem',
            new_name='OrderItem',
        ),
        migrations.AddField(
            model_name='order',
            name='coupon',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='orders', to='coupons.coupon', verbose_name='Купон'),
        ),
        migrations.AddField(
            model_name='order',
            name='discount',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)]),
        ),
        migrations.AlterField(
            model_name='order',
            name='last_name',
            field=models.CharField(max_length=50, verbose_name='Прізвище'),
        ),
    ]
