# Generated by Django 3.2.8 on 2022-04-20 03:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_product_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='date_updated',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]