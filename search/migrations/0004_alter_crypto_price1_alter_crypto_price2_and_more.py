# Generated by Django 4.1.4 on 2023-01-27 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0003_remove_crypto_pattern_crypto_price1_crypto_price2_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crypto',
            name='price1',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='crypto',
            name='price2',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='crypto',
            name='price3',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='crypto',
            name='price4',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='crypto',
            name='price5',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
