from django.contrib import admin
from django.conf.urls import url, include
from app import views, api_control

# IP/


urlpatterns = [
    url(r'^login', views.login, name="login"),
    url(r'^register', views.register, name="register"),
    url(r'^homepage', views.homepage, name="homepage"),
    url(r'^search', views.search_user, name="search"),
    url(r'^logout', views.logout, name="logout"),
    url(r'^search_restaurant', views.search_restaurant, name="search_restaurant"),
    url(r'^api/get_events', views.get_events, name="get_events"),
    url(r'^api/login', api_control.login, name="login"),
    url(r'^api/register', api_control.register, name="register"),
    url(r'^api/create_event', api_control.create_event, name="create_event"),
]
