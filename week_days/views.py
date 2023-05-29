from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
# Create your views here.

days_description = {'monday':'1. дело, 2. дело, 3.дело', 'tuesday':'1. дело, 2. дело', 'wednesday':'1. дело',
                    'thursday':'нет дел', 'friday':'1. дело, 2. дело, 3. дело', 'saturday': '1. дело',
                    'sunday': 'нету дел'}


def day_viewer_ofweek(request, day_url: str):
    discript = days_description.get(day_url)
    if discript:
        return HttpResponse(discript)
    else:
        return HttpResponseNotFound('Нет такого названия дня недели.')

def day_viewer_number(request, day_url: int):
    if (day_url <= 7) and (day_url > 0):
        days_list = list(days_description)
        day = days_list[day_url-1]
        redirect_url = reverse('week-name', args=(day, ))
        return HttpResponseRedirect(redirect_url)
    else:
        return HttpResponseNotFound(f'Неверный номер дня - {day_url}')

def greeting(request):
    return render(request, 'week_days/greeting_page.html')

def info_about_west(request, object_url):
    object_url = object_url.lower()
    if object_url == 'kianu':
        context = {'year_born': 1964,
                    'city_born': 'Бейрут',
                    'movie_name': 'На гребне волны'}
        return render(request, 'week_days/Kianu_riffs.html', context=context)
    elif object_url == 'guiness':
        context = {'power_man': 'Narve Laeret',
                   'bar_name': 'Bob\'s BBQ & Grill',
                   'count_needle': 1790}
        return render(request, 'week_days/guinnessworldrecords.html', context=context)
    else:
        return HttpResponseNotFound('Такой страницы нет.')
