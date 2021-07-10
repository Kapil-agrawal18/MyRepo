from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("",views.index, name='home'),
    path("index_2", views.index_2, name='index_2'),
    path("about", views.about, name='about'),
    path("help", views.help, name='help'),
    path("login", views.login, name='login'),
    path("items", views.items, name='items'),
]
