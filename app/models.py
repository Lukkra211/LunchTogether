from django.db import models


class Rating(models.Model):
    aggregate_rating = models.FloatField()
    rating_text = models.CharField(max_length=60)
    rating_color = models.CharField(max_length=10)
    votes = models.IntegerField()

    def __str__(self):
        return str(self.aggregate_rating)


class Location(models.Model):
    address = models.CharField(max_length=200)
    locality = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    city_id = models.CharField(max_length=100)
    latitude = models.CharField(max_length=100)
    longitude = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=20)
    locality_verbose = models.CharField(max_length=100)
    country_id = models.CharField(max_length=100)

    def __str__(self):
        return str(self.address)


class Restaurant(models.Model):
    name = models.CharField(max_length=60)
    location = models.ForeignKey(Location, blank=True, null=True)
    rating = models.ForeignKey(Rating, blank=True, null=True)
    has_table_booking = models.BooleanField(default=True)
    has_online_delivery = models.BooleanField(default=True)
    average_cost_for_two = models.CharField(max_length=60)
    menu = models.TextField(max_length=300)

    def __str__(self):
        return str(self.name)


class TagRestaurant(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return str(self.name)


class RestaurantHasTagRestaurant(models.Model):
    restaurant = models.ForeignKey(Restaurant)
    tag = models.ForeignKey(TagRestaurant)

    def __str__(self):
        return str(self.restaurant) + " - " + str(self.tag)


class Event(models.Model):
    time = models.DateTimeField()
    note = models.TextField(max_length=300)
    restaurant = models.ForeignKey(Restaurant, blank=True, null=True)

    def __str__(self):
        return str(self.time) + " - " + str(self.restaurant)


class TagEvent(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return str(self.name)


class EventHasTag(models.Model):
    tag = models.ForeignKey(TagEvent)
    event = models.ForeignKey(Event)

    def __str__(self):
        return str(self.tag) + " - " + str(self.event)


class User(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    mail = models.EmailField()

    event = models.ForeignKey(Event, blank=True, null=True)
    frineds = models.ManyToManyField("self", through='Contact', symmetrical=False, related_name="contact_set")

    def right_user(self, username, password):
        if username == self.username and self.password == password:
            return True
        return False

    def is_registred(self, username):
        if username == self.username:
            return True
        return False

    def __str__(self):
        return str(self.username)


class Contact(models.Model):
    user1 = models.ForeignKey(User, related_name="contact_set1")
    user2 = models.ForeignKey(User, related_name="contact_set2")
    confirmed = models.BooleanField()

    def __str__(self):
        return str(self.user1) + " - " + str(self.user2)