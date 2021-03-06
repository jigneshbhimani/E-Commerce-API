# Generated by Django 3.2.5 on 2021-07-02 06:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('date_created', models.DateField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'Categories',
                'ordering': ['-date_created'],
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=50)),
                ('tag', models.CharField(max_length=10, unique=True)),
                ('availablity', models.BooleanField(default=True)),
                ('price', models.FloatField(max_length=10)),
                ('discount', models.FloatField(max_length=10)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('description', models.CharField(max_length=500)),
                ('date_created', models.DateField(auto_now_add=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='api_basic.category')),
            ],
            options={
                'ordering': ['category', 'tag', 'price'],
            },
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('cart_id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('quantity', models.IntegerField(max_length=5)),
                ('categories', models.ManyToManyField(to='api_basic.Category')),
                ('products', models.ManyToManyField(to='api_basic.Product')),
            ],
            options={
                'ordering': ['cart_id', '-created_at'],
            },
        ),
    ]
