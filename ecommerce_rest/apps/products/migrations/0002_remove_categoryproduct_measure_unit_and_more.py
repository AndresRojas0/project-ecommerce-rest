# Generated by Django 5.1.5 on 2025-01-22 12:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='categoryproduct',
            name='measure_unit',
        ),
        migrations.RemoveField(
            model_name='historicalcategoryproduct',
            name='measure_unit',
        ),
        migrations.AddField(
            model_name='historicalproduct',
            name='category_product',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='products.categoryproduct', verbose_name='Categoría de Producto'),
        ),
        migrations.AddField(
            model_name='historicalproduct',
            name='measure_unit',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='products.measureunit', verbose_name='Unidad de Medida'),
        ),
        migrations.AddField(
            model_name='product',
            name='category_product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='products.categoryproduct', verbose_name='Categoría de Producto'),
        ),
        migrations.AddField(
            model_name='product',
            name='measure_unit',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='products.measureunit', verbose_name='Unidad de Medida'),
        ),
    ]
