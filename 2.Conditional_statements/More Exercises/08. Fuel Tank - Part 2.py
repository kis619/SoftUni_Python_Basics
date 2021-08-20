type_of_fuel = input()
litres = float(input())
club_card = input()

gasoline = 2.22 # бензин
diesel = 2.33
gas = 0.93

if club_card == "Yes":
    gasoline -= .18
    diesel -= .12
    gas -= .08

if type_of_fuel == "Gasoline":
    price = litres * gasoline
elif type_of_fuel == "Diesel":
    price = litres * diesel
elif type_of_fuel == "Gas":
    price = litres * gas

if 20 <= litres <= 25:
    price *= .92
elif litres > 25:
    price *= .9

print(f"{price:.2f} lv.")