# Generated by Django 3.1.5 on 2021-07-14 05:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api_basic', '0017_auto_20210714_1058'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cart',
            options={'ordering': ['cart', '-created_at']},
        ),
        migrations.RenameField(
            model_name='cart',
            old_name='user',
            new_name='cart',
        ),
    ]
