budget = int(input())
season = input()
fishermen = int(input())

boat_rent = 0
if season == "Spring":
    boat_rent = 3000
elif season == "Summer" or season == "Autumn":
    boat_rent = 4200
elif season == "Winter":
    boat_rent = 2600

if fishermen <= 6:
    boat_rent *= .9
elif fishermen <= 11:
    boat_rent *= .85
else:
    boat_rent *= .75

if not season == "Autumn" and fishermen % 2 == 0:
    boat_rent *= .95

difference = abs(budget - boat_rent)
if budget < boat_rent:
    print(f"Not enough money! You need {difference:.2f} leva.")
else:
    print(f"Yes! You have {difference:.2f} leva left.")