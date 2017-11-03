# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from models import Trader
from django import forms
from django.core.validators import RegexValidator
#from django.shortcuts import render


# Create your views here.
def register_trader(request):

    if request.method == "POST":
        form = RegistrationFormTrader(request.POST)
        if form.is_valid():
            trader = Trader.object.create(
                name=form.cleaned_data('name'),
                surname=form.cleaned_data('surname'),
                birthday=form.cleaned_data('birthday'),
                country=form.cleaned_data('country'),
                mail_code=form.cleaned_data('mail_code'),
                address=form.cleaned_data('address'),
                phone_number=form.cleaned_data('phone_number'),
                email=form.cleaned_data('email'),
                password=form.cleaned_data('password'),
                password_repeat=form.cleaned_data('password_repeat'),
                logo=form.cleaned_data('logo'),
                link_facebook=form.cleaned_data('link_facebook'),
                link_linkedIn=form.cleaned_data('link_linkedIn'),
                invest_time=form.cleaned_data('invest_time'),
                investments=form.cleaned_data('investments'),
                add_info=form.cleaned_data('add_info'),
            )
            trader.save()
            return #Возвращаем объект json, чтобы кидать ошибки на js на фронте
    else:
        return #


class RegistrationFormTrader(forms.Form):
    name = forms.CharField(
        max_length=100,
        required=True,
        error_messages={'required': 'Please enter your name',
                        'max_length': 'max length = 100 characters'}
    )
    surname = forms.CharField(
        max_length=100,
        required=True,
        error_messages={'required': 'Please enter your surname',
                        'max_length': 'max length = 100 characters'}
    )
    birthday = forms.DateField(
        required=True,
        error_messages={'required': 'Please enter your birthday',
                        'invalid': '%Y-%m-%d, %m/%d/%Y, %m/%d/%y'}
    )
    country = forms.CharField(
        max_length=50,
        required=True,
        error_messages={'required': 'Please enter your country',
                        'max_length': 'max length = 50 characters'}
    )
    #Сколько может быть цифр максимально в почтовом коде?
    validator_mail_code = RegexValidator(regex=r'\d{10-20}', message='invalid mail code')
    mail_code = forms.CharField(
        validators=validator_mail_code,
        required=True,
        error_messages={'required': 'Please enter your country'}
    )
    address = forms.CharField(
        required=True,
        max_length=150,
        error_messages={'required': 'Please enter your country',
                        'max_length': 'max length = 150 characters'}
    )
    phone_number = forms.CharField(
        phone_regex=RegexValidator(regex=r'\d{9,15}$',
                                   message="Phone number must be entered in the format:")

    )
    email = forms.EmailField(
        required=True,
        error_messages={'required': 'Please enter your email'}
    )
    password = forms.CharField(
        #Валидатор на условия
        #Узнать как хешировать и солировать пароль
    )
    password_repeat = forms.CharField(

    )
    logo = forms.ImageField(
        #links
    )
    link_facebook = forms.CharField(
        required=False,
        error_message={}

    )
    link_linkedIn = forms.CharField(
        required=False,
        error_messages={}
    )
    invest_time = forms.CharField(
        #validator
    )
    investments = forms.BooleanField(
        required=False

    )
    add_info = forms.CharField(
        required=False,
        max_length=2000,
        error_messages={'max_length': 'max length 2000 characters'}
    )

    def clean(self):
        cleaned_data = super(RegistrationFormTrader, self).clean()
        password = cleaned_data.get("password")
        password_repeat = cleaned_data.get("password_repeat")
        if password != password_repeat:
            raise forms.ValidationError("Password repeat does not match")


#То же самое для фонда