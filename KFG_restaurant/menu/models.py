import django.contrib.auth.forms
from django.db import models
from django.db.models import ManyToManyField, ForeignKey, CharField, DateField, TimeField,\
    IntegerField, BooleanField, FloatField, TextField
from datetime import date, time
from django.contrib.auth.models import User


class Category(models.Model):
    name = CharField(max_length=150, unique=True)

    def __str__(self):
        return self.name.title()


class Product(models.Model):
    name = CharField(max_length=150)
    price = FloatField()
    description = TextField()
    category = ForeignKey(Category, on_delete=models.CASCADE)


class Combo(models.Model):
    products = ForeignKey(Product, on_delete=models.CASCADE)
    is_action = BooleanField(default=False)
    is_basket = BooleanField(default=False)
    price = FloatField()

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
    time_out = TimeField(null=True)
    complete = BooleanField(default=False)
    bring_with = BooleanField(default=False)
    staff_id = ForeignKey(Staff, on_delete=models.CASCADE)

    def time_out_true(self):
        if self.time_out == True:
            self.time_out.auto_now()
            self.complete = "True"
        else:
            pass


class ProductOrderList(models.Model):
    product = ForeignKey(Product, on_delete=models.CASCADE)
    product_order = ForeignKey(ProductOrder, on_delete=models.CASCADE)