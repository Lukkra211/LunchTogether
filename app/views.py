from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.http import JsonResponse
from app.models import User
import logging
import websockets
import asyncio

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
        return HttpResponse("POST DONE-uživatel nenalezen")


def register(request):
    if request.method == "GET":
        return HttpResponse("Get metoda k ničemu")
    if request.method == "POST":
        username = request.POST.get("username", "")
        password = request.POST.get("password", "")
        logger.error(username)
        for user in User.objects.all():
            if user.is_registred(username):
                return HttpResponse("Tento uživatel je již registrován")
        if username != "" and password != "":
            User(username=username, password=password).save()
            return HttpResponse("")
        return HttpResponse("Chyba: zadal prázdný jsi email nebo heslo")


def homepage(request):
    def start():
        websocket = websockets.connect('ws://localhost:8765')

    server = websockets.serve(start, 'localhost', 8765)
    asyncio.get_event_loop().run_until_complete(server)
    asyncio.get_event_loop().run_forever()
