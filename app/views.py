from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.http import JsonResponse
from app.models import User
import logging

logger = logging.getLogger(__name__)


def login(request):
    if request.method == "GET":
        return HttpResponse("Get metoda k ničemu")
    if request.method == "POST":
        username = request.POST.get("username","")
        password = request.POST.get("password","")
        for user in User.objects.all():
            if user.right_user(username, password):
                # account found
                request.session["username"] = username
                return JsonResponse({"user_id": user.id})
        return HttpResponse("POST DONE-uživatel nenalezen")


def register(request):
    return False