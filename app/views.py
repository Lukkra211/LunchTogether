from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from app.models import User, Event
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


def get_events(request):
    user_id = request.POST.get("user_id", "")
    aktiv_event_id = ""
    if user_id != "":

        list_event = []
        for event in Event.objects.all():
            list_event.append(
                {"id": event.id, "time": str(event.time), "name": event.name, "note": event.note})

        list_user = []
        for user in User.objects.all():
            if user.event != None:
                event_id = user.event.id
            else:
                event_id = "nenalezen event"
            list_user.append({"user_id": user.id, "name": user.username, "event": event_id, "mail": user.mail})
            if user.id == user_id:
                aktiv_event_id = user.event.id

        json = {"events": list_event, "users": list_user, "user_belongs_to": aktiv_event_id}
        return JsonResponse(json)


def homepage(request):
    pass
