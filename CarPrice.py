def carPrice(make):
    if make == "toyota":
        return 30000
    elif make == "honda":
        return 28000
    elif make == "ford":
        return 25000
    else:
        return 0

car_make = input("Enter the car make (Toyota, Honda, Ford): ").strip().lower()
print("The price of the car is:", carPrice(car_make))