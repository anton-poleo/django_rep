# -*- coding: utf-8 -*-
from __future__ import unicode_literals
# import json
from PIL import Image
from models import Trader, Fund
from django import forms
from django.core.validators import RegexValidator
from django.http import HttpResponse
# from django.template import loader
# from django.core.validators import ValidationError
from django.shortcuts import render
from django.http import JsonResponse
# Функция принимает form_id и вызвывает нужную регистрацию. Или здесь считывать id, тогда объединить формы.
# Класс формы все поля по html. Заполняем, валидируем, что ужно конкатенируем и отправляем в model.create
# Create your views here.


def registration(request):
    if request.method == "POST":
        if request.POST['form_id'] == 'trader':
            form = RegistrationFormTrader(request.POST, request.FILES)
            if form.is_valid():
                # image = Image.open(request.FILES['logo'])
                trader = Trader.objects.create(
                    name=form.cleaned_data.get('name'),
                    surname=form.cleaned_data.get('surname'),
                    birthday=form.cleaned_data.get('birthday'),
                    country=form.cleaned_data.get('country'),
                    mail_code=form.cleaned_data.get('mail_code'),
                    address=form.cleaned_data.get('address'),
                    phone_number=form.cleaned_data.get('first_part_phone_number') + form.cleaned_data.get(
                        'second_part_phone_number'),
                    email=form.cleaned_data.get('email'),
                    password=form.cleaned_data.get('password'),
                    # password_repeat=form.cleaned_data.get('password_repeat'),
                    logo=form.cleaned_data.get('logo'),
                    link_facebook=form.cleaned_data.get('link_facebook'),
                    link_linkedIn=form.cleaned_data.get('link_linkedIn'),
                    invest_time=form.cleaned_data.get('invest_year') + ":" + form.cleaned_data.get('invest_month'),
                    investments=form.cleaned_data.get('radio_name1'),
                    add_info=form.cleaned_data.get('add_info')
                )
                trader.save()
                # редиректим на проверку номера, а затем в личный кабинет
                return JsonResponse({"status": True})
            else:
                return JsonResponse({"status": False, "message": {"error": form.errors}})

        else:
            form = RegistrationFormFund(request.POST, request.FILES)
            if form.is_valid():
                fund = Fund.objects.create(
                    name_fund=form.cleaned_data.get('name_fund'),
                    country=form.cleaned_data.get('country'),
                    mail_code=form.cleaned_data.get('mail_code'),
                    address=form.cleaned_data.get('address'),
                    name_leader=form.cleaned_data.get('name_leader'),
                    surname_leader=form.cleaned_data.get('surname_leader'),
                    birthday=form.cleaned_data.get('birthday'),
                    phone_number=form.cleaned_data.get('first_part_phone_number') + form.cleaned_data.get(
                        'second_part_phone_number'),
                    email=form.cleaned_data.get('email'),
                    password=form.cleaned_data.get('password'),
                    logo=form.cleaned_data.get('logo'),
                    age_of_fund=form.cleaned_data.get('age_of_fund_year') + ':' + form.cleaned_data.get(
                        'age_of_fund_month'),
                    img_leader=form.cleaned_data.get('img_leader'),
                    link_facebook=form.cleaned_data.get('link_facebook'),
                    link_linkedIn=form.cleaned_data.get('link_linkedIn'),
                    add_info_fund=form.cleaned_data.get('add_info_fund'),
                    add_info_leader=form.cleaned_data.get('add_info_leader')
                )
                fund.save()
                # редиректим на проверку номера, от туда в личный кабинет
                return JsonResponse({"status": True})
            else:
                return JsonResponse({"status": False, "message": {"error": form.errors}})

    else:
        return render(request, 'registration/registration.html')


def index(request):
    return render(request, 'registration/registration.html')


def reg_test(request):
    if request.method == "POST":
        form = RegistrationFormFund(request.POST)
        if form.is_valid():
            type_of = type(form['age_of_fund_year'])
            return HttpResponse(type_of)
        else:
            c = form.errors.as_json()
            return HttpResponse(c)
    else:
        form = RegistrationFormFund()
        return render(request, 'registration/registration.html', {'form': form})


def register_trader(request):
    if request.method == "POST":
        form = RegistrationFormTrader(request.POST)
        if form.is_valid():
            trader = Trader.objects.create(
                name=form.cleaned_data.get('name'),
                surname=form.cleaned_data.get('surname'),
                birthday=form.cleaned_data.get('birthday'),
                country=form.cleaned_data.get('country'),
                mail_code=form.cleaned_data.get('mail_code'),
                address=form.cleaned_data.get('address'),
                phone_number=form.cleaned_data.get('first_part_phone_number') + form.cleaned_data.get(
                    'second_part_phone_number'),
                email=form.cleaned_data.get('email'),
                password=form.cleaned_data.get('password'),
                logo=form.cleaned_data.get('logo'),
                link_facebook=form.cleaned_data.get('link_facebook'),
                link_linkedIn=form.cleaned_data.get('link_linkedIn'),
                invest_time=form.cleaned_data.get('invest_year') + ":" + form.cleaned_data.get('invest_month'),
                radio_name1=form.cleaned_data.get('radio_name1'),
                add_info=form.cleaned_data.get('add_info')
            )
            trader.save()
            # редиректим на проверку номера, а затем в личный кабинет
            return HttpResponse("eee")
        else:
            return JsonResponse({'Status': False, 'message': {'errors': form.errors}})
    else:
        form = RegistrationFormTrader()
        return render(request, 'registration/registration.html', {'form': form})


def register_fund(request):

    if request.method == "POST":
        form = RegistrationFormFund(request.POST)
        if form.is_valid():
            fund = Fund.objects.create(
                name_fund=form.cleaned_data.get('name_fund'),
                country=form.cleaned_data.get('country'),
                mail_code=form.cleaned_data.get('mail_code'),
                address=form.cleaned_data.get('address'),
                name_leader=form.cleaned_data.get('name_leader'),
                surname_leader=form.cleaned_data.get('surname_leader'),
                birthday=form.cleaned_data.get('birthday'),
                phone_number=form.cleaned_data.get('first_part_phone_number') + form.cleaned_data.get(
                    'second_part_phone_number'),
                email=form.cleaned_data.get('email'),
                password=form.cleaned_data.get('password'),
                logo=form.cleaned_data.get('logo'),
                age_of_fund=form.cleaned_data.get('age_of_fund_year') + ':' + form.cleaned_data.get(
                    'age_of_fund_month'),
                img_leader=form.cleaned_data.get('img_leader'),
                link_facebook=form.cleaned_data.get('link_facebook'),
                link_linkedIn=form.cleaned_data.get('link_linkedIn'),
                add_info_fund=form.cleaned_data.get('add_info_fund'),
                add_info_leader=form.cleaned_data.get('add_info_leader')
            )
            fund.save()
            # редиректим на проверку номера, от туда в личный кабинет
            return HttpResponse("eee")
        else:
            # Возвращаем ошиб
            return HttpResponse(form.errors.as_json())
    else:
        form = RegistrationFormTrader()
        return render(request, 'registration/registration.html', {'form': form})


class RegistrationFormTrader(forms.Form):
    name = forms.CharField(
        label='Имя',
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
                        'invalid': 'Please enter your birthday in format:'
                                   '%Y-%m-%d, %m/%d/%Y, %m/%d/%y'}
    )
    country = forms.CharField(
        max_length=50,
        required=True,
        error_messages={'required': 'Please enter your country',
                        'max_length': 'max length = 50 characters'}
    )
    validator_mail_code = RegexValidator(regex=r'^\d{5,20}$',
                                         message='invalid mail code',
                                         )
    mail_code = forms.CharField(
        validators=[validator_mail_code],
        required=True,
        error_messages={'required': 'Please enter your mail code',
                        }
    )
    address = forms.CharField(
        required=True,
        max_length=100,
        error_messages={'required': 'Please enter your country',
                        'max_length': 'max length = 100 characters'}
    )

    first_part_phone_number = forms.CharField(
        required=True,
        error_messages={'required': 'Please enter your phone'}
    )
    phone_regex = RegexValidator(regex=r'^\d{10}$',
                                 message="Phone number must be entered in the format: xxxxxxxxxx"
                                 )
    second_part_phone_number = forms.CharField(
        validators=[phone_regex],
        required=True,
        error_messages={'required': 'Please enter your phone'}
    )
    email = forms.EmailField(
        required=True,
        error_messages={'required': 'Please enter your email'}
    )
    password = forms.CharField(
        min_length=6,
        max_length=100,
        required=True,
        error_messages={'required': 'Please enter your password',
                        'min_length': 'min length 6 characters'}
    )
    password_repeat = forms.CharField(
        required=True,
        error_messages={'required': 'Please repeat your password'}
    )
    logo = forms.ImageField(
        # links
        required=False
    )
    link_facebook = forms.CharField(
        empty_value=None,
        required=False,
    )
    link_linkedIn = forms.CharField(
        empty_value=None,
        required=False,
    )

    invest_year = forms.CharField(
        max_length=2,
        error_messages={'max_length': 'max length 2 characters',
                        'required': 'Please enter your invest time'}
    )
    invest_month = forms.CharField(
        max_length=2,
        error_messages={'max_length': 'max length 2 characters',
                        'required': 'Please enter your invest time'}
    )

    radio_name1 = forms.CharField(
        max_length=100,
        required=False
    )
    add_info = forms.CharField(
        empty_value=None,
        required=False,
        max_length=2000,
        error_messages={'max_length': 'max length 2000 characters',
                        }
    )

    def clean(self):
        cleaned_data = super(RegistrationFormTrader, self).clean()
        password = cleaned_data.get("password")
        password_repeat = cleaned_data.get("password_repeat")
        if password != password_repeat:
            raise forms.ValidationError("Password repeat does not match")


class RegistrationFormFund(forms.Form):
    name_fund = forms.CharField(
        max_length=100,
        required=True,
        error_messages={"required": "Please enter your fund's name",
                        "max_length": "max length 100 character"}
    )
    country = forms.CharField(
        max_length=50,
        required=True,
        error_messages={'required': 'Please enter your country',
                        'max_length': 'max length = 50 characters'}
    )
    validator_mail_code = RegexValidator(regex=r'\d{5,20}', message='invalid mail code')
    mail_code = forms.CharField(
        validators=[validator_mail_code],
        required=True,
        error_messages={'required': 'Please enter your mail code'}
    )
    address = forms.CharField(
        required=True,
        max_length=150,
        error_messages={'required': 'Please enter your country',
                        'max_length': 'max length = 150 characters'}
    )
    name_leader = forms.CharField(
        max_length=100,
        required=True,
        error_messages={'required': 'Please enter your name',
                        'max_length': 'max length = 100 characters'}
    )
    surname_leader = forms.CharField(
        max_length=100,
        required=True,
        error_messages={'required': 'Please enter your surname',
                        'max_length': 'max length = 100 characters'}
    )
    birthday = forms.DateField(
        required=True,
        error_messages={'required': 'Please enter your birthday',
                        'invalid': 'Please enter your birthday in format:'
                                   '%Y-%m-%d, %m/%d/%Y, %m/%d/%y'}
    )
    first_part_phone_number = forms.CharField(
        required=True,
        max_length=3
    )
    phone_regex = RegexValidator(regex=r'^\d{10}$',
                                 message="Phone number must be entered in the format:"
                                         " '+999999999'. Up to 15 digits allowed.")
    second_part_phone_number = forms.CharField(
        required=True,
        validators=[phone_regex],
        max_length=10,
        error_messages={'required': 'Please enter your phone'}
    )
    email = forms.EmailField(
        required=True,
        error_messages={'required': 'Please enter your email'}
    )
    password = forms.CharField(
        required=True,
        max_length=100,
        min_length=6,
        error_messages={'required': 'Please enter your password',
                        'min_length': 'min length 6 characters'}
    )
    password_repeat = forms.CharField(
        required=True,
        max_length=100,
        min_length=6,
        error_messages={'required': 'Please repeat your password'}
    )
    logo = forms.ImageField(
        required=False
    )
    age_of_fund_year = forms.CharField(
        required=True,
        max_length=3,
        error_messages={'required': 'Please enter age of your fund'}
    )
    age_of_fund_month = forms.CharField(
        required=True,
        max_length=3,
        error_messages={'required': 'Please enter age of your fund'}
    )
    img_leader = forms.ImageField(
        required=False
    )
    link_facebook = forms.CharField(
        required=False,
        max_length=100
    )
    link_linkedIn = forms.CharField(
        required=False,
        max_length=100
    )
    add_info_fund = forms.CharField(
        max_length=2000,
        required=False,
        error_messages={'required': 'Please enter your country',
                        'max_length': 'max length = 50 characters'}

    )
    add_info_leader = forms.CharField(
        max_length=2000,
        required=False,
        error_messages={'required': 'Please enter your country',
                        'max_length': 'max length = 50 characters'}

    )

    def clean(self):
        cleaned_data = super(RegistrationFormFund, self).clean()
        password = cleaned_data.get("password")
        password_repeat = cleaned_data.get("password_repeat")
        if password != password_repeat:
            raise forms.ValidationError("Password repeat does not match")
