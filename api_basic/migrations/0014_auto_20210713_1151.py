# Generated by Django 3.1.5 on 2021-07-13 06:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api_basic', '0013_auto_20210713_1119'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cart',
            options={'ordering': ['cart_id', '-created_at']},
        ),
        migrations.RemoveField(
            model_name='cart',
            name='id',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='paid',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='updated_at',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='user_id',
        ),
        migrations.AddField(
            model_name='cart',
            name='cart_id',
            field=models.OneToOneField(default=7, on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='auth.user'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cart',
            name='products',
            field=models.ManyToManyField(to='api_basic.Product'),
        ),
        migrations.AddField(
            model_name='cart',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
        migrations.DeleteModel(
            name='OrderItem',
        ),
    ]