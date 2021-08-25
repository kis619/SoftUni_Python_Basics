budget = int(input())
season = input()
fishermen = int(input())

# boat_rent_spring = 3000
# boat_rent_summer_and_autumn = 4200
# boat_rent_winter = 2600
boat_rent = 0
if season == "Spring":
    boat_rent = 3000
elif season == "Winter":
    boat_rent = 2600
else:
    boat_rent = 4200

discount = 0
if fishermen <= 6:
    discount = .1 * boat_rent #boat_rent *= .9
elif 7 <= fishermen <= 11: # fishermen <= 11
    discount = .15 * boat_rent
else:
    discount = .25 * boat_rent

additional_discount = 0
if fishermen % 2 == 0 and season != "Autumn": # if fishermen % 2 == 0 and not season == "Autumn"
    additional_discount = (boat_rent - discount) * .05

final_amount = boat_rent - discount - additional_discount
money_difference = abs(budget - final_amount)

if budget >= final_amount:
    print(f"Yes! You have {money_difference:.2f} leva left.")
else:
    print(f"Not enough money! You need {money_difference:.2f} leva.")