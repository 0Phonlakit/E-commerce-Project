# Generated by Django 3.2.16 on 2023-12-13 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_auto_20231211_2151'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='cases',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='product',
            name='cpu_cooler',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='product',
            name='monitor',
            field=models.BooleanField(default=False),
        ),
    ]
