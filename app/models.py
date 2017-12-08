from django.db import models


# Create your models here.
class Restaurant(models.Model):
    name = models.CharField(max_length=60)
    location = models.TextField(max_length=300)
    food_type = models.CharField(max_length=60)
    has_table_booking = models.BooleanField(default=True)
    has_online_delivery = models.BooleanField(default=True)
    average_cost_for_two = models.CharField(max_length=60)
    user_rating = models.TextField(max_length=300)


class Event(models.Model):
    time = models.DateTimeField()
    note = models.TextField(max_length=300)
    restaurant = models.ForeignKey(Restaurant)


class User(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    event = models.ForeignKey(Event)

    def right_user(self, username, password):
        if username == self.username and self.password == password:
            return True
        return False

    def get_id(self):
        return self.id

    def is_registred(self, username):
        if username == self.username:
            return True
        return False