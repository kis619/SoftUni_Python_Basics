fuel_type = input()
fuel_litres = float(input())
# if fuel_type != ""
if fuel_litres >= 25 and (fuel_type == "Gasoline" or fuel_type == "Diesel" or fuel_type == "Gas"):
    print(f"You have enough {str.lower(fuel_type)}.")
elif fuel_litres < 25 and (fuel_type == "Gasoline" or fuel_type == "Diesel" or fuel_type == "Gas"):
    print(f"Fill your tank with {str.lower(fuel_type)}!")
else:
    print("Invalid fuel!")
