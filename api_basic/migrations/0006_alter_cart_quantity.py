# Generated by Django 3.2.5 on 2021-07-02 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_basic', '0005_remove_cart_categories'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
    ]
