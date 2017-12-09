import logging

from django.http import JsonResponse
from django.shortcuts import render, HttpResponse, redirect

from app.models import User, TagRestaurant, Restaurant, Event

logger = logging.getLogger(__name__)


def login(request):
    if request.method == "GET":
        if request.session["username"]:
            return redirect("/homepage")
        return render(request, "../templates/login.html")
    if request.method == "POST":
        username = request.POST.get("username", "")
        password = request.POST.get("password", "")
        logger.error(username)
        for user in User.objects.all():
            if user.right_user(username, password):
                request.session["username"] = username
                return redirect("/homepage")
        return JsonResponse({"user_id": "-1"})


def register(request):
    if request.method == "GET":
        if request.session["username"]:
            return redirect("/homepage")
        return render(request, "../templates/register.html")
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
            return redirect("/homepage")
        return HttpResponse("Chyba: zadal prázdný jsi email nebo heslo")


def homepage(request):
    if request.method == "GET":
        if not request.session["username"]:
            return redirect("/login")
        all_events = Event.objects.all()
        return render(request,"../templates/index.html",{"all_events":all_events})
    if request.method == "POST":
        return HttpResponse("Get metoda k ničemu")


def create_event(request):
    if request.method == "GET":
        return HttpResponse("Get metoda k ničemu")
    if request.method == "POST":
        tag = request.POST.get("tag", "")
        time = request.POST.get("time", "")
        name = request.POST.get("name", "")
        note = request.POST.get("note", "")
        event = Event.objects.get_or_create(time=time, tag=tag, name=name, note=note)[0]
        return HttpResponse("Get metoda k ničemu")


def join_event(request):
    if request.method == "POST":
        tag = request.POST.get("time", "")
        name = request.POST.get("name", "")
        username = request.session['username']
        User.objects.get(username=username).update(event=Event.objects.filter(tag=tag, name=name))
        return HttpResponse("Get metoda k ničemu")


def search_user(request):
    if request.method == "GET":
        return render(request, '../templates/graphs.static', )
    if request.method == "POST":
        friend = request.POST.get("username", "")
        username = request.session['username']
        User.objects.get(username=username).add_friend(friend)

        return render(request, '../templates/graphs.static',
                      {})

def logout(request):
    print("test")
    request.session['username']=""
    return redirect("/login")

def search_restaurant(request):
    if request.method == "GET":
        return render(request, '../templates/graphs.static',
                      {})
    if request.method == "POST":
        sort_by_rating = request.POST.get("sort", True)
        tag = request.POST.get("tag", "")
        name = request.POST.get("name", "")
        restaurants = Restaurant.objects.filter(TagRestaurant=TagRestaurant.objects.get(name=tag), name__contains=name)
        if sort_by_rating:
            restaurants = restaurants.order_by('rating__aggregate_rating')
        return render(request, '../templates/graphs.static',
                      {"restaurants": restaurants})
