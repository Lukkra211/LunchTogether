from django.shortcuts import render, HttpResponse, redirect

from app.models import User, TagRestaurant, Restaurant, Event

from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from app.models import User, Event
import logging

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
    if request.method == "GET":
        if not request.session["username"]:
            return redirect("/login")
        all_events = Event.objects.all()
        return render(request, "../templates/index.html", {"all_events": all_events})
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
        Event(time=time, tag=tag, name=name, note=note).save()
        return redirect("/homepage")


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
            event = event.filter(tag=tag)
        if time_from:
            event = event.filter(time__gte=time_from, time__lte=time_to)
        if name:
            event = event.filter(name=name)

        return render(request, "../templates/index.html", {"all_events": event})


def join_event(request):
    if request.method == "POST":
        tag = request.POST.get("time", "")
        name = request.POST.get("name", "")
        username = request.session['username']
        User.objects.get(username=username).update(event=Event.objects.filter(tag=tag, name=name))
        return HttpResponse("Get metoda k ničemu")


def search_user(request):
    if request.method == "GET":
        return render(request, '../templates/index.html', )
    if request.method == "POST":
        friend = request.POST.get("username", "")
        username = request.session['username']
        User.objects.get(username=username).add_friend(friend)
        return redirect("/homepage")


def logout(request):
    print("test")
    request.session['username'] = ""
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
