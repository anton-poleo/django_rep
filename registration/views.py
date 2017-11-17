# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from models import Trader, Fund, Investor
from django import forms
from django.core.validators import RegexValidator
from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from django.contrib.auth.models import User, Permission
from django.contrib.auth import authenticate, login
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.decorators import permission_required
import random
# from django.shortcuts import redirect

content_type = ContentType.objects.get(app_label='registration', model='access')
permission = Permission.objects.get_or_create(codename='rights',
                                              name='Global customer rights',
                                              content_type=content_type)


def send_code(phone, code):
    return True


def test(request):
    request.session['name'] = 'anton'
    return HttpResponse(request.session)


@permission_required('registration.rights')
def test2(request):
    if request.method == 'POST':
        form = VerificationForm(request.POST)
        if form.is_valid():
            if request.session['code'] == form.cleaned_data.get('code'):
                return HttpResponse('User')
            else:
                return HttpResponse('None')
        else:
            return JsonResponse({"status": False,
                                 "message": {"error": form.errors}})
    else:
        return render(request, 'registration/verification.html')


def code_generator():
    count = 0
    result = ''
    while count != 4:
        result += str(random.randint(0, 9))
        count += 1
    return result


def registration(request):
    if request.method == "POST":
        if request.POST['form_id'] == 'trader':
            form = RegistrationFormTrader(request.POST, request.FILES)
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
                    logo=form.cleaned_data.get('logo'),
                    link_facebook=form.cleaned_data.get('link_facebook'),
                    link_linkedIn=form.cleaned_data.get('link_linkedIn'),
                    invest_time=form.cleaned_data.get('invest_year') + ":" + form.cleaned_data.get('invest_month'),
                    investments=form.cleaned_data.get('radio_name1'),
                    add_info=form.cleaned_data.get('add_info')
                    # добавляем код в базу данных?
                )
                trader.save()

                # создаем пользователя
                user = User.objects.create_user(username=form.cleaned_data.get('email'),
                                                password=form.cleaned_data.get('password'))
                user.save()
                user.user_permissions.add(permission)
                # аутентифицируем пользователя в системе
                user = authenticate(username=form.cleaned_data.get('email'),
                                    password=form.cleaned_data.get('password'))

                if user is not None:
                    if user.is_active:
                        login(request, user)
                        # Redirect to a success page.
                    else:
                        return JsonResponse
                # Return a 'disabled account' error message

                else:
                    return JsonResponse
                # Return an 'invalid login' error message.

                # генерируем проверочный код для верификации
                code = code_generator()

                # ___________________________________исправить высылаемовый код пользователю____________________________
                # ______________________________________________________________________________________________________
                request.session['code'] = '1111'

                # отправляем сгенерированный код на номер телефона
                # если не доставлено, то делаем что-то
                if not send_code(code, form.cleaned_data.get('phone_number')):
                    pass

                return JsonResponse({'status': True,
                                     "message": "/registration/test2/"})
            else:
                return JsonResponse({"status": False,
                                     "message": {"error": form.errors}})
                # return HttpResponse(request.session)

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

                # user = User.objects.create_user(username=form.cleaned_data.get('email'),
                #                                password=form.cleaned_data.get('password'))
                # user.save()
                # user = authenticate(username=form.cleaned_data.get('email'),
                #                    password=form.cleaned_data.get('password'))
                # редиректим на проверку номера, от туда в личный кабинет
                return JsonResponse({'status': True,
                                     "message": "/registration/verification/"})
            else:
                return JsonResponse({"status": False,
                                     "message": {"error": form.errors}})

    else:
        return render(request, 'registration/registration.html')


def registration_investor(request):
    if request.method == "POST":
        form = RegistrationFormInvestor(request.POST)
        if form.is_valid():
            investor = Investor.objects.create(
                name=form.cleaned_data.get('name'),
                surname=form.cleaned_data.get('surname'),
                country=form.cleaned_data.get('country'),
                phone_number=form.cleaned_data.get('first_part_phone_number') + form.cleaned_data.get(
                    'second_part_phone_number'),
                email=form.cleaned_data.get('email'),
            )
            investor.save()
            # редиректим на проверку номера, а затем в личный кабинет
            return JsonResponse({'status': True, "message": "/registration/verification/"})
        else:
            return JsonResponse({'status': False, 'message': {'errors': form.errors}})
    else:
        return render(request, 'registration/reg_investor.html')


def reg_test(request):
    if request.method == "POST":
        form = RegistrationFormInvestor(request.POST)
        if form.is_valid():
            return JsonResponse({"status": True})
        else:
            return JsonResponse({"status": False, "message": {"error": form.errors}})
    else:
        return render(request, 'registration/reg_investor.html')


def verification(request):
    if request.method == "POST":
        form = VerificationForm(request.POST)
        if form.is_valid():
            if form.code == request.session['code']:

                # request.user.user_permission.add(permission)
                return JsonResponse({'status': True})
            else:
                return JsonResponse({'status': False, 'message': 'invalid code'})
        else:
            return JsonResponse({'status': False, 'message': 'Please, enter the code'})
    else:
        return render(request, 'registration/verification.html')


class VerificationForm(forms.Form):
    code = forms.CharField(
        max_length=10,
        required=True
    )


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
    phone_regex = RegexValidator(regex=r'^\d{9,15}$',
                                 message="Invalid phone number"
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
        required=False,
    )
    link_linkedIn = forms.CharField(
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
        required=False,
        max_length=2000,
        error_messages={'max_length': 'max length 2000 characters',
                        }
    )
    agreement = forms.CharField(
        required=True,
        error_messages={'required': 'please '}
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
    phone_regex = RegexValidator(regex=r'^\d{10,15}$',
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
    agreement = forms.CharField(
        required=True,
        error_messages={'required': 'please '}
    )

    def clean(self):
        cleaned_data = super(RegistrationFormFund, self).clean()
        password = cleaned_data.get("password")
        password_repeat = cleaned_data.get("password_repeat")
        if password != password_repeat:
            raise forms.ValidationError("Password repeat does not match")


class RegistrationFormInvestor(forms.Form):
    name = forms.CharField(
        max_length=100,
        required=True,
        error_messages={"required": "Please enter your name",
                        "max_length": "max length 100 character"}
    )
    surname = forms.CharField(
        max_length=100,
        required=True,
        error_messages={"required": "Please enter your surname",
                        "max_length": "max length 100 character"}
    )
    country = forms.CharField(
        max_length=100,
        required=True,
        error_messages={"required": "Please enter your country",
                        "max_length": "max length 100 character"}
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
        error_messages={'required': 'Please enter your password',
                        'min_length': 'min length 6 characters'}
    )
    agreement = forms.CharField(
        required=True,
        error_messages={'required': 'please '}
    )

    def clean(self):
        cleaned_data = super(RegistrationFormInvestor, self).clean()
        password = cleaned_data.get("password")
        password_repeat = cleaned_data.get("password_repeat")
        if password != password_repeat:
            raise forms.ValidationError("Password repeat does not match")
