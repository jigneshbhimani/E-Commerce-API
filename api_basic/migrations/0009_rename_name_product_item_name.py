# Generated by Django 3.2.5 on 2021-07-02 06:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api_basic', '0008_rename_item_product_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='name',
            new_name='item_name',
        ),
    ]