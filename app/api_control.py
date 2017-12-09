import logging

from django.http import JsonResponse
from django.shortcuts import render, HttpResponse

from app.models import User, TagRestaurant, Restaurant, Event

logger = logging.getLogger(__name__)

def register(request):
    if request.method == "GET":
        return HttpResponse("")
    if request.method == "POST":
        username = request.POST.get("username", "")
        password = request.POST.get("password", "")
        mail = request.POST.get("mail", "")
        logger.error(username)
        for user in User.objects.all():
            if user.is_registred(username):
                return HttpResponse("Tento uživatel je již registrován")
        if username != "" and password != "":
            request.session['username'] = username
            User(username=username, password=password, mail=mail).save()
            return HttpResponse("")
        return HttpResponse("Chyba: zadal prázdný jsi email nebo heslo")


def login(request):
    if request.method == "GET":
        return HttpResponse("")
    if request.method == "POST":
        username = request.POST.get("username", "")
        password = request.POST.get("password", "")
        logger.error(username)
        for user in User.objects.all():
            if user.right_user(username, password):
                # account found
                request.session["username"] = username
                return JsonResponse({"user_id": user.id})
        return JsonResponse({"user_id": "-1"})

def search_event(request):
    if request.method == "GET":
        return HttpResponse("Get metoda k ničemu")
    if request.method == "POST":
        tag = request.POST.get("tag", "")
        time_from = request.POST.get("time_from", "")
        time_to = request.POST.get("time_to", "")
        name = request.POST.get("name", "")
        event = Event.objects.all()
        if tag:
            event.filter(tag=tag)
        if time_from:
            event.filter(time__gte=time_from,time__lte=time_to)
        if tag:
            event.filter(name=name)
        if tag:
            event.filter(tag=tag)

        return HttpResponse(event)
