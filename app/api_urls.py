from django.contrib import admin
from django.conf.urls import url, include
from app import api_control
#IP/api/
urlpatterns = [
    url('login', api_control.login, name="login"),
    url('register', api_control.register, name="register"),
]