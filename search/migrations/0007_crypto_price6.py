# Generated by Django 4.1.4 on 2023-01-28 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0006_alter_crypto_trend'),
    ]

    operations = [
        migrations.AddField(
            model_name='crypto',
            name='price6',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
