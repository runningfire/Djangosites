# -*- coding: utf-8 -*-
"""
Created on Mon May  8 01:32:00 2023

@author: home
"""
from django.urls import path, register_converter
from . import views as views_horo
from . import converters


register_converter(converters.FourDigitYearConverter, "yyyy")
register_converter(converters.MyFloatConverter, "my_float")
register_converter(converters.MyDateConverter, "my_date")

urlpatterns = [
    path('', views_horo.index),
    path("<my_date:url_zodiac>", views_horo.get_my_date_converters),
    path("type", views_horo.element_index),
    path("16/", views_horo.get_info_about_16),
    path("type/<element>", views_horo.element_description, name='element-name'),
    path("<yyyy:url_zodiac>", views_horo.get_yyyy_converters),
    path("<int:url_zodiac>", views_horo.get_info_url_zodiac_by_number),
    path("<my_float:url_zodiac>", views_horo.get_float_converters),
    path("<str:url_zodiac>", views_horo.get_info_url_zodiac, name='horoscope-name'),
    path("<int:month>/<int:day>", views_horo.day_and_month)
    ]
