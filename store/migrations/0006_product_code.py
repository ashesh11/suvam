# Generated by Django 3.2.8 on 2022-04-13 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_auto_20220318_1936'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='code',
            field=models.TextField(default='N/A', max_length=15, null=True),
        ),
    ]