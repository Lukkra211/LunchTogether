from django.db import models


class TagRestaurant(models.Model):
    name = models.CharField(max_length=30)


class Restaurant(models.Model):
    name = models.CharField(max_length=60)
    location = models.TextField(max_length=300)
    TagRestaurant = models.ForeignKey(TagRestaurant, null=True)
    has_table_booking = models.BooleanField(default=True)
    has_online_delivery = models.BooleanField(default=True)
    average_cost_for_two = models.CharField(max_length=60)
    user_rating = models.TextField(max_length=300)


class Event(models.Model):
    time = models.DateTimeField()
    note = models.TextField(max_length=300)
    restaurant = models.ForeignKey(Restaurant, null=True)


class TagEvent(models.Model):
    name = models.CharField(max_length=30)


class EventHasTag(models.Model):
    tag = models.ForeignKey(TagEvent)
    event = models.ForeignKey(Event)


class User(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    mail = models.EmailField()

    event = models.ForeignKey(Event, null=True)
    friends = models.ManyToManyField("self")

    def right_user(self, username, password):
        if username == self.username and self.password == password:
            return True
        return False

    def is_registred(self, username):
        if username == self.username:
            return True
        return False

