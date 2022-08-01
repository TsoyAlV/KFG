import django.contrib.auth.forms
from django.db import models
from django.db.models import ManyToManyField, ForeignKey, CharField, DateField, TimeField, \
    IntegerField, BooleanField, FloatField, TextField
from datetime import date, time
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator


class Category(models.Model):
    name = CharField(max_length=150, unique=True)

    def __str__(self):
        return self.name.title()


class Product(models.Model):
    name = CharField(max_length=150)
    price = FloatField(default=0)
    description = TextField(null=True)
    category = ForeignKey(Category, on_delete=models.CASCADE)
    quantity = IntegerField(default=1)


class Combo(models.Model):
    products = ManyToManyField(Product, through='QuantityProduct')
    is_action = BooleanField(default=False)
    is_basket = BooleanField(default=False)
    price = FloatField(default=0, validators=[MinValueValidator(0.0)])


class QuantityProduct(models.Model):
    product = ForeignKey(Product, on_delete=models.CASCADE)
    combo = ForeignKey(Combo, on_delete=models.CASCADE)
    quantity = IntegerField(default=1, null=True)


class Staff(models.Model):
    choices_staff = [
        ('CA', "Cashier"),
        ('AD', "Administrator"),
        ('DI', "Director"),
    ]
    staff = CharField(max_length=2, choices=choices_staff)
    user_id = ForeignKey(User, on_delete=models.CASCADE)


class ProductOrder(models.Model):
    product = ManyToManyField(Product, through="ProductOrderList")
    date = DateField(auto_now=True)
    time_in = TimeField(auto_now=True)
    time_out = TimeField(auto_now=True, null=True)
    complete = BooleanField(default=False)
    bring_with = BooleanField(default=False)
    staff_id = ForeignKey(Staff, on_delete=models.CASCADE)

    def completed(self):
        self.complete = True


class ProductOrderList(models.Model):
    product = ForeignKey(Product, on_delete=models.CASCADE)
    quantity = IntegerField(default=1)
    product_order = ForeignKey(ProductOrder, on_delete=models.CASCADE)
