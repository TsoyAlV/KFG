# Generated by Django 4.0.6 on 2022-07-28 22:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('price', models.FloatField()),
                ('description', models.TextField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='menu.category')),
            ],
        ),
        migrations.CreateModel(
            name='ProductOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now=True)),
                ('time_in', models.TimeField(auto_now=True)),
                ('time_out', models.TimeField(null=True)),
                ('complete', models.BooleanField(default=False)),
                ('bring_with', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('staff', models.CharField(choices=[('CA', 'Cashier'), ('AD', 'Administrator'), ('DI', 'Director')], max_length=2)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ProductOrderList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='menu.product')),
                ('product_order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='menu.productorder')),
            ],
        ),
        migrations.AddField(
            model_name='productorder',
            name='product',
            field=models.ManyToManyField(through='menu.ProductOrderList', to='menu.product'),
        ),
        migrations.AddField(
            model_name='productorder',
            name='staff_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='menu.staff'),
        ),
        migrations.CreateModel(
            name='Combo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_action', models.BooleanField(default=False)),
                ('is_basket', models.BooleanField(default=False)),
                ('price', models.FloatField()),
                ('products', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='menu.product')),
            ],
        ),
    ]
