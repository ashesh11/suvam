# Generated by Django 3.2.8 on 2022-04-20 08:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_alter_product_date_updated'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='store.category'),
        ),
        migrations.AlterField(
            model_name='product',
            name='code',
            field=models.TextField(blank=True, default='N/A', max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='promotion',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='store.promotion'),
        ),
    ]
