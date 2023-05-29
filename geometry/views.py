from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from math import pi
# Create your views here.

def get_rectangle_area(request, width, height):
    if (width == 0) or (height == 0):
        text = '<h2>Ширина или длина равна 0</h2>'
    else:
        text = f'<h2>Площадь прямоугольника размером {width}X{height} равна {width*height}</h2>'
    return render(request, 'geometry/rectangle.html')

def get_square_area(request, width):
    if width == 0:
        text = '<h2>Ширина равна 0</h2>'
    else:
        text = f'<h2>Площадь квадрата размером {width}X{width} равна {width**2}</h2>'
    return render(request, 'geometry/square.html')

def get_circle_area(request, radius):
    if radius == 0:
        text = '<h2>Радиус равен 0</h2>'
    else:
        area_circle = round(pi * radius**2)
        text = f'<h2>Площадь круга с радиусом {radius} равна {area_circle}</h2>'
    return render(request, 'geometry/circle.html')

def redirect_rectangle(request, width, height):
    redirect_url = reverse('rectangle', args=(width, height))
    return HttpResponseRedirect(redirect_url)

def redirect_square(request, width):
    redirect_url = reverse('square', args=(width, ))
    return HttpResponseRedirect(redirect_url)

def redirect_circle(request, radius):
    redirect_url = reverse('circle', args=(radius, ))
    return HttpResponseRedirect(redirect_url)