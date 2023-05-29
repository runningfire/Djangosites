from django.urls import path
from . import views as views_week

urlpatterns = [
    path('info_about_west/<str:object_url>/', views_week.info_about_west),
    path('', views_week.greeting),
    path('<int:day_url>/', views_week.day_viewer_number),
    path('<str:day_url>/', views_week.day_viewer_ofweek, name='week-name'),
    ]
