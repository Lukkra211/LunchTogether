from django.contrib import admin
from django.conf.urls import url, include
from app import views
#IP/api/
urlpatterns = [
    url('login', views.login, name="login"),
]