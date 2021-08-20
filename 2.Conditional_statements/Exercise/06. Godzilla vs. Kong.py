budget = float(input())
extras = int(input())
price_clothes_per_extra = float(input())
# result = f"{pari:.2f}
decor = 0.1 * budget

if extras > 150:
    price_clothes_per_extra *= 0.9

spendings = extras * price_clothes_per_extra + decor
surplus = budget - spendings
insufficient = spendings - budget
if spendings > budget:
    print("Not enough money!")
    print(f"Wingard needs {insufficient:.2f} leva more.")
else:
    print("Action!")
    print(f"Wingard starts filming with {surplus:.2f} leva left.")
