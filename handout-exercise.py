def hotel_cost(nights):
    return nights * 140


def plane_ride_cost(city):
    pass
    if "capetown" == city:
        return 2500
    elif "Durban" == city:
        return 2300
    elif "JHB" == city:
        return 2000
    elif "BFN" == city:
        return 1800
    else:
        return "The location not in our database"

# defining a rental car cost
# cost is in rands

def rental_car_cost(days):
    car_cost = 40 * days

    if days >= 7:
        car_cost = car_cost - 50
    elif days >= 3 and days < 7:
        car_cost = car_cost - 20
    return car_cost

def trip_cost(city, days, spending_money):
    return rental_car_cost(days) + plane_ride_cost(city) + spending_money


location = input("Where did you go: ")
days = int(input("How many days?: "))
extras = float(input("Any extra money you spent?: "))
print(trip_cost(location, days, extras))