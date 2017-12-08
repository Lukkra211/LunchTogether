from django.contrib import admin
from django.conf.urls import url, include
from app import views
urlpatterns = [
    url('login', views.login, name="login"),
    url('register', views.register, name="register"),
]