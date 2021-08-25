budget = float(input())
season = input()

destination = ''
if budget <= 100:
    destination = "Bulgaria"
elif budget <= 1000:
    destination = "Balkans"
else:
    destination = "Europe"

expenses = 0
if destination == "Bulgaria":
    if season == "summer":
        expenses = .3 * budget
    else:
        expenses = .7 * budget
elif destination == "Balkans":
    if season == "summer":
        expenses = .4 * budget
    else:
        expenses = .8 * budget
else:
    expenses = .9 * budget

accommodation = ""
if season == "summer" and destination != "Europe":
    accommodation = "Camp"
else:
    accommodation = "Hotel"

print(f"Somewhere in {destination}")
print(f"{accommodation} - {expenses:.2f}")