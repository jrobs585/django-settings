# -*- coding: utf-8 -*-
from django.contrib import admin
from django.utils.translation import ugettext as _
from django.contrib.contenttypes import generic
from django_settings import models, forms


def get_setting_value(obj):
    data = obj.setting_object.value
    ellipsified = (data[:70] + '...') if len(data) > 73 else data
    return ellipsified
get_setting_value.short_description = _('Value')


class SettingAdmin(admin.ModelAdmin):
    model = models.Setting
    form = forms.SettingForm
    list_display = ('name', 'setting_type', get_setting_value)
admin.site.register(models.Setting, SettingAdmin)
