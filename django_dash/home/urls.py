from django.urls import path
from . import views
from home.dash_apps.finished_apps import MessivsRonaldo
from home.dash_apps.finished_apps import owners
from home.dash_apps.finished_apps import interactive


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about')
]