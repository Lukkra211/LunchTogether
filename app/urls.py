from django.contrib import admin
from django.conf.urls import url, include
from app import views

# IP/

urlpatterns = [
    url('login', views.login, name="login"),
    url('register', views.register, name="register"),
    url('homepage', views.homepage, name="homepage"),
    url('search', views.search_user, name="search"),
    url('logout', views.logout, name="logout"),
    url('search_restaurant', views.search_restaurant, name="search_restaurant"),
    url('get_events', views.get_events, name="get_events"),
]
