# Generated by Django 3.2.16 on 2023-12-14 14:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cartitem',
            old_name='products',
            new_name='product',
        ),
    ]