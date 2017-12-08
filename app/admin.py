from django.contrib import admin

# Register your models here.

from .models import User,Restaurant,Event,TagEvent,EventHasTag,TagRestaurant
admin.site.register(User)
admin.site.register(Restaurant)
admin.site.register(Event)
admin.site.register(TagEvent)
admin.site.register(EventHasTag)
admin.site.register(TagRestaurant)