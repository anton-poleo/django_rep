# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from models import Trader, Fund, Investor

# Register your models here.
admin.site.register(Trader)
admin.site.register(Fund)
admin.site.register(Investor)
