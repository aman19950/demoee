from django.contrib import admin
from django.urls import path

from . import views
urlpatterns = [

    path("", views.index,name="home"),
    path("contact/", views.contact, name="contact"),
    path("save/", views.saveinfo, name="save"),
    path("login/", views.login, name="login"),
    path("logout/", views.logout, name="logout"),


]
