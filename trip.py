def hotel_cost(night):
    return 140*night
def flight_cost(city):
    if(city == "chandigar"):
        return 185
    elif(city== "chennai"):
        return 190
    elif(city == "delhi"):
        return 200
def car_cost(days):
    if(days>=7):
        return 40*days - 50
    elif(days>=3):
        return 40*days - 20
    else:
        return 40*days
def trip_cost(city, days, spentmoney):
    return hotel_cost(days)+ flight_cost(city)+car_cost(days)+ spentmoney
print("cost of hotel ", hotel_cost(5))
print("cost of flight ", flight_cost("chennai"))
print("cost of car ", car_cost(5))
print("total trip cost ", trip_cost("chennai",5,25000))