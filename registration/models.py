# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models


class Trader(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    birthday = models.DateField()
    country = models.CharField(max_length=100)
    mail_code = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15, blank=True)
    email = models.EmailField()
    logo = models.ImageField(upload_to='img', default=None, blank=True)
    link_facebook = models.CharField(max_length=100, default=None)
    link_linkedIn = models.CharField(max_length=100, default=None)
    # инвестиции в активы. гг:мм
    invest_time = models.CharField(max_length=100)
    # инвестировали ли вы до этого
    investments = models.CharField(max_length=10)
    add_info = models.CharField(max_length=2000)

    class Meta:
        db_table = "trader"


class Fund(models.Model):
    name_fund = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    mail_code = models.IntegerField()
    address = models.CharField(max_length=100)
    name_leader = models.CharField(max_length=100)
    surname_leader = models.CharField(max_length=100)
    birthday = models.DateField()
    phone_number = models.CharField(max_length=15, blank=True)
    email = models.EmailField()
    logo = models.ImageField(upload_to='img', default=None, blank=True)
    # Форматирование гг.мм
    age_of_fund = models.CharField(max_length=100)
    img_leader = models.ImageField(upload_to='img', default=None, blank=True)
    link_facebook = models.CharField(max_length=100)
    link_linkedIn = models.CharField(max_length=100)
    add_info_fund = models.CharField(max_length=2000)
    add_info_leader = models.CharField(max_length=2000)

    class Meta:
        db_table = "fund"


class Investor(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    email = models.CharField(max_length=100)

    class Meta:
        db_table = "investor"


class Access(models.Model):

    class Meta:

        managed = False

        permissions = (
            ('customer_rights', 'Global customer rights'),
        )
