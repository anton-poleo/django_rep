# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from models import Trader, Fund
from django import forms
from django.core.validators import RegexValidator
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
# Функция принимает form_id и вызвывает нужную регистрацию. Или здесь считывать id, тогда объединить формы.
# Класс формы все поля по html. Заполняем, валидируем, что ужно конкатенируем и отправляем в model.create
# Create your views here.


def registration(request):
    if request.method == "POST":
        if request.POST['form_id'] == 'trader':
            return register_trader(request)
        else:
            return register_fund(request)


def index(request):
    return render(request, 'registration/registration.html')


def reg_test(request):
    if request.method == "POST":
        form = RegistrationFormTrader(request.POST)
        if form.is_valid():
            return HttpResponse(form)
        else:
            a = request.POST.get('second_part_phone_number')
            return HttpResponse(form.errors)
    else:
        form = RegistrationFormTrader()
        return render(request, 'registration/registration.html', {'form': form})


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
                phone_number=form.cleaned_data('first_part_phone_number') + form.cleaned_data('second_part_phone_number'),
                email=form.cleaned_data('email'),
                password=form.cleaned_data('password'),
                password_repeat=form.cleaned_data('password_repeat'),
                logo=form.cleaned_data('logo'),
                link_facebook=form.cleaned_data('link_facebook'),
                link_linkedIn=form.cleaned_data('link_linkedIn'),
                invest_time=form.cleaned_data('invest_year')+form.cleaned_data('invest_month'),
                investments=True,
                add_info=form.cleaned_data('add_info')
            )
            trader.save()

            return render(request, '/registration/verification.html', {'form': form})
        else:
            # Возвращаем объект json
            return render(request, '/registration/registration.html', {'form': form})
    else:
        form = RegistrationFormTrader()
        return render(request, 'registration/registration.html', {'form': form})


def register_fund(request):

    if request.method == "POST":
        form = RegistrationFormFund(request.POST)
        if form.is_valid():
            fund = Fund.object.create(
                name_fund=form.cleaned_data('name_fund'),
                country=form.cleaned_data('country'),
                mail_code=form.cleaned_data('mail_code'),
                address=form.cleaned_data('address'),
                name_leader=form.cleaned_data('name'),
                surname_leader=form.cleaned_data('surname'),
                birthday=form.cleaned_data('birthday'),
                phone_number=form.cleaned_data('phone_number'),
                email=form.cleaned_data('email'),
                password=form.cleaned_data('password'),
                password_repeat=form.cleaned_data('password_repeat'),
                logo=form.cleaned_data('logo'),
                age_of_fund=form.cleaned_data('age_of_fund'),
                img_leader=form.cleaned_data('img_leader'),
                link_facebook=form.cleaned_data('link_facebook'),
                link_linkedIn=form.cleaned_data('link_linkedIn'),
                invest_time=form.cleaned_data('invest_time'),
                investments=form.cleaned_data('investments'),
                add_info_fund=form.cleaned_data('add_info_fund'),
                add_info_leader=form.cleaned_data('add_info_leader')
            )
            fund.save()
            # редиректим на проверку номера, от туда в личный кабинет
            return 1
        else:
            # Возвращаем ошибку. json???
            return 1
    else:
        form = RegistrationFormTrader()
        return render(request, 'registration/index.html', {'form': form})


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
                        'invalid': '%Y-%m-%d, %m/%d/%Y, %m/%d/%y'}
    )
    country = forms.CharField(
        max_length=50,
        required=True,
        error_messages={'required': 'Please enter your country',
                        'max_length': 'max length = 50 characters'}
    )
    # Сколько может быть цифр максимально в почтовом коде?
    validator_mail_code = RegexValidator(regex=r'^[0-9]{5-20}',
                                         message='invalid mail code')
    mail_code = forms.CharField(
        validators=[validator_mail_code],
        required=True,
        error_messages={'required': 'Please enter your mail code',
                        }
    )
    address = forms.CharField(
        required=True,
        max_length=150,
        error_messages={'required': 'Please enter your country',
                        'max_length': 'max length = 150 characters'}
    )
    phone_regex = RegexValidator(regex=r'^\d{10}$',
                                 message="Phone number must be entered in the format:")
    first_part_phone_number = forms.CharField(
        # validators=[phone_regex],
        required=True,
        error_messages={'required': 'Please enter your phone'}
    )
    second_part_number_phone = forms.CharField(
        validators=[phone_regex],
        required=True,
        error_messages={'required': 'Please enter your phone'}
    )
    email = forms.EmailField(
        required=True,
        error_messages={'required': 'Please enter your email'}
    )
    # validator_password = RegexValidator(regex=r'')
    password = forms.CharField(
        required=True,
        error_messages={'required': 'Please enter your phone'}
        # Валидатор на условия
        # Узнать как хешировать и солировать пароль
    )
    password_repeat = forms.CharField(
        required=True,
        error_messages={'required': 'Please enter your phone'}
    )
    # logo = forms.ImageField(
        # links
    # )
    link_facebook = forms.CharField(
        required=False,
    )
    link_linkedIn = forms.CharField(
        required=False,
    )
    invest_time = forms.CharField(
    #     validator
    )
    investments = forms.BooleanField(
        required=False

    )
    add_info = forms.CharField(
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


# То же самое для фонда
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
    validator_mail_code = RegexValidator(regex=r'\d{10-20}', message='invalid mail code')
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
                        'invalid': '%Y-%m-%d, %m/%d/%Y, %m/%d/%y'}
    )
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format:"
                                         " '+999999999'. Up to 15 digits allowed.")
    phone_number = forms.CharField(

    )
    email = forms.EmailField(
        required=True,
        error_messages={'required': 'Please enter your email'}
    )
    password = forms.CharField(

    )
    password_repeat = forms.CharField(

    )
    logo = forms.ImageField(

    )
    age_of_fund = forms.CharField(

    )
    img_leader = forms.ImageField(

    )
    link_facebook = forms.CharField(
        required=False,

    )
    link_linkedIn = forms.CharField(
        required=False
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
