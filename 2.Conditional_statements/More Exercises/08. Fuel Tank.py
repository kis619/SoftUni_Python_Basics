fuel_type = input()
fuel_litres = float(input())
# if fuel_type != ""
if fuel_litres >= 25:
    if fuel_type == "Gasoline":
        fuel_type = "gasoline"
        print(f"You have enough {fuel_type}.")
    elif fuel_type == "Diesel":
        fuel_type = "diesel"
        print(f"You have enough {fuel_type}.")
    elif fuel_type == "Gas":
        fuel_type = "gas"
        print(f"You have enough {fuel_type}.")
    else:
        print("Invalid fuel!")
else:
    if fuel_type != "Gasoline" and fuel_type != "Diesel" \
        and fuel_type != "Gas":
        print("Invalid fuel!")
    else:
        print(f"Fill your tank with {str.lower(fuel_type)}!")
