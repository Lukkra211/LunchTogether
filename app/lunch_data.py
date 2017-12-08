from app import query_api

for i in range(5):
    print(i)
    response = query_api.Query().search_restaurant(entity_id=93, entity_type="city",start=20*i)
    if response!={}:
        for restaurant in response["restaurants"]:
            info= restaurant["restaurant"]
            print(info)
            print(info["average_cost_for_two"])
            print(info["currency"])
            print(info["user_rating"])
            print(info["has_table_booking"])
            print(info["has_online_delivery"])
            print(info["menu_url"])
            print(info["cuisines"])
            print(info["url"])
            print(info["id"])
            print(info["name"])
            print(info["url"])
            print(info["location"])
