from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from app.models import User
import logging


logger = logging.getLogger(__name__)


def login(request):
    if request.method == "GET":
        return HttpResponse("Get metoda k ničemu")
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


def register(request):
    if request.method == "GET":
        return HttpResponse("Get metoda k ničemu")
    if request.method == "POST":
        username = request.POST.get("username", "")
        password = request.POST.get("password", "")
        mail = request.POST.get("mail", "")
        logger.error(username)
        for user in User.objects.all():
            if user.is_registred(username):
                return HttpResponse("Tento uživatel je již registrován")
        if username != "" and password != "":
            User(username=username, password=password, mail=mail).save()
            return HttpResponse("")
        return HttpResponse("Chyba: zadal prázdný jsi email nebo heslo")


def homepage(request):
    pass