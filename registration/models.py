# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.core.validators import RegexValidator
# Create your models here.
# Убрать все валидаторы. Проверки во вьюшке
'''
    name
    surname
    born_date
    country
    mail_code
    address
    phone_number
    email
    password
    logo
    link_facebook
    link_linkedIn
    invest_time
    investments
    add_info
'''

class Trader(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    born_date = models.DateField()
    country = models.CharField(max_length=100)
    # аргументы??
    mail_code = models.CharField(max_length=100)
    # Придумать проверку, либо написать поле
    address = models.CharField(max_length=100)
    phone_regex = RegexValidator(regex=r'\d{9,15}$',
                                 message="Phone number must be entered in the format:")
    # validators should be a list
    # проверить поле  r'^\+?1?\d{9,15}$',
    phone_number = models.CharField(validators=[phone_regex], max_length=15, blank=True)  # validators should be a list
    email = models.EmailField()
    password = models.CharField(max_length=100)
    # Доп инфа или анкета трейдера
    logo = models.ImageField()
    link_facebook = models.CharField(max_length=100)
    link_linkedIn = models.CharField(max_length=100)
    # инвестиции в активы. гг:мм
    invest_regex = RegexValidator(regex=r'([0-30]{0,1})*:([0-11]{0,1})',
                                  message="invalid date")
    # validators=invest_regex
    invest_time = models.CharField(max_length=100)
    investments = models.BooleanField(default=False)
    add_info = models.CharField(max_length=100)

    class Meta:

        db_table = "trader"


class Fund(models.Model):

    name_fund = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    mail_code = models.IntegerField()
    # Придумать проверку, либо написать поле
    address = models.CharField(max_length=100)
    name_leader = models.CharField(max_length=100)
    surname_leader = models.CharField(max_length=100)
    birthday = models.DateField()

    # аргументы??
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format:"
                                         " '+999999999'. Up to 15 digits allowed.")
    # validators should be a list
    # проверить поле
    phone_number = models.CharField(validators=[phone_regex], max_length=15, blank=True)  # validators should be a list
    email = models.EmailField()
    password = models.CharField(max_length=100)
    # Доп инфа или анкета трейдера
    logo = models.ImageField()
    # Форматирование гг.мм + регулярка для проверки
    age_of_fund = models.CharField(max_length=100)
    img_leader = models.ImageField()
    link_facebook = models.CharField(max_length=100)
    link_linkedIn = models.CharField(max_length=100)
    add_info_fund = models.CharField(max_length=2000)
    add_info_leader = models.CharField(max_length=2000)

    class Meta:
        db_table = "fund"
