
from app import query_api
from .models import Restaurant, TagRestaurant, Location, Rating

i = 0
response = query_api.Query().search_restaurant(entity_id=93, entity_type="city", start=20 * i)
if response != {}:
    for restaurant in response["restaurants"]:
        info = restaurant["restaurant"]

        tag = TagRestaurant.objects.get_or_create(name=info["cuisines"])
        location = Location.objects.get_or_create(address=info["address"], locality=info["locality"],
                                                  city=info["city"], city_id=info["city_id"],
                                                  latitude=info["latitude"], longitude=info["longitude"],
                                                  locality_verbose=info["locality_verbose"],
                                                  zipcode=info["zipcode"], country_id=info["country_id"])
        rating = Rating.objects.get_or_create(aggregate_rating=info["aggregate_rating"],
                                              rating_text=info["rating_text"], rating_color=info["rating_color"],
                                              votes=info["votes"])
        booking = True
        if info["has_table_booking"] == 0:
            booking = False
        online_delivery = True
        if info["has_online_delivery"] == 0:
            online_delivery = False
        avg_for_two = str(info["average_cost_for_two"] + " " + info["currency"])
        user_rating = "aggregate_rating:" + info["user_rating"]["aggregate_rating"]
        if Restaurant.objects.filter(name=info["name"], TagRestaurant=tag, has_table_booking=booking,
                                     average_cost_for_two=avg_for_two,
                                     menu=info['menu_url'], rating=rating, location=location).exists():
            Restaurant(name=info["name"], TagRestaurant=tag, has_table_booking=booking,
                       average_cost_for_two=avg_for_two,
                       menu=info['menu_url'], rating=rating, location=location)

        print(info["user_rating"])
        print(info["location"])