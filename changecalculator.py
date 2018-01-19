import math

coin_values = [.25, .10, .05, .01]

def get_price():
    test = True
    while test:
        try:
            return float(input("Enter price: "))
        except ValueError:
            test = True

def get_payment():
    test = True
    while test:
        try:
            return float(input("Enter payment: "))
        except ValueError:
            test = True

def get_change():
    price = get_price()
    payment = get_payment()
    return payment - price

def coin_totals(cv):
    coins = []
    remainder = get_change()
    for i in cv:
        coins.append(math.floor(remainder / i))
        remainder = remainder % i
    return coins

def main():
    coins = coin_totals(coin_values)
    print("{0} quarters, {1} dimes, {2} nickels and {3} pennies.".format(*coins))

while True:
    main()
