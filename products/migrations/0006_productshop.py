# Generated by Django 5.0.4 on 2024-05-07 05:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_alter_product_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductShop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product')),
            ],
            options={
                'verbose_name': 'Shop',
                'verbose_name_plural': 'Shops',
            },
        ),
    ]
