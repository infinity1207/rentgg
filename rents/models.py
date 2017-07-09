#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils import six

@python_2_unicode_compatible
class Product(models.Model):
    UNIT_CHOICES = (
        ('m', '米'),
        ('pcs', '个'),
    )
    name = models.CharField(max_length=100)
    price = models.FloatField()
    unit = models.CharField(max_length=10, choices=UNIT_CHOICES)

    def __str__(self):
        return self.name

@python_2_unicode_compatible
class Customer(models.Model):
    name = models.CharField(max_length=100)
    tel = models.CharField(max_length=20)

    def __str__(self):
        return self.name

@python_2_unicode_compatible
class Rent(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    happen_date = models.DateField()
    out_or_in = models.BooleanField(default=True)   #out: 借, in: 还
    remark = models.TextField(blank=True)

    create_date = models.DateField(auto_now_add=True)
    last_modified_date = models.DateField(auto_now=True)

    def __str__(self):
        return self.customer.name

@python_2_unicode_compatible
class RentDetail(models.Model):
    rent = models.ForeignKey(Rent)
    product = models.ForeignKey(Product)
    count = models.IntegerField()

    def __str__(self):
        return "%s - %s%s" % (self.product.name, count, self.product.unit)
