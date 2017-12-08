"""ADD funcition: at the end of the month check all websites and continue getting data"""

from django.core.management.base import BaseCommand

from app import query_api
from ...models import Restaurant, TagRestaurant, Location, Rating, RestaurantHasTagRestaurant


class Command(BaseCommand):
    def handle(self, *args, **options):
        for i in range(5):
            response = query_api.Query().search_restaurant(entity_id=93, entity_type="city", start=20 * i)
            if response != {}:
                for restaurant in response["restaurants"]:
                    info = restaurant["restaurant"]

                    location = Location.objects.get_or_create(address=info["location"]["address"],
                                                              locality=info["location"]["locality"],
                                                              city=info["location"]["city"],
                                                              city_id=str(info["location"]["city_id"]),
                                                              latitude=info["location"]["latitude"],
                                                              longitude=info["location"]["longitude"],
                                                              locality_verbose=info["location"]["locality_verbose"],
                                                              zipcode=info["location"]["zipcode"],
                                                              country_id=str(info["location"]["country_id"]))[0]

                    rating = Rating.objects.get_or_create(aggregate_rating=info["user_rating"]["aggregate_rating"],
                                                          rating_text=info["user_rating"]["rating_text"],
                                                          rating_color=info["user_rating"]["rating_color"],
                                                          votes=info["user_rating"]["votes"])[0]

                    booking = True
                    if info["has_table_booking"] == 0:
                        booking = False
                    online_delivery = True
                    if info["has_online_delivery"] == 0:
                        online_delivery = False
                    avg_for_two = str(info["average_cost_for_two"]) + " " + info["currency"]

                    if not Restaurant.objects.filter(name=info["name"], location=location).exists():
                        Restaurant(name=info["name"], has_table_booking=booking,
                                   average_cost_for_two=avg_for_two,
                                   menu=info['menu_url'], rating=rating, location=location,
                                   has_online_delivery=online_delivery).save()
                    else:
                        Restaurant.objects.filter(name=info["name"], location=location).update(
                            average_cost_for_two=avg_for_two,
                            menu=info['menu_url'], rating=rating,
                            has_online_delivery=online_delivery)

                    restaurant = Restaurant.objects.get(name=info["name"], location=location)
                    tag = TagRestaurant.objects.get_or_create(name=info["cuisines"])[0]
                    if not RestaurantHasTagRestaurant.objects.filter(tag=tag, restaurant=restaurant).exists():
                        RestaurantHasTagRestaurant(tag=tag, restaurant=restaurant).save()
