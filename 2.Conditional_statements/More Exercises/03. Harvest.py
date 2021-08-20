from math import floor
from math import ceil

area = int(input())
grapes_per_square_meter = float(input())
wine_needed = int(input())
workers = int(input())

area_grapes_for_wine = .4 * area
kilograms_grapes_for_wine = area_grapes_for_wine * grapes_per_square_meter
wine_produced = kilograms_grapes_for_wine / 2.5
wine_difference = abs(wine_produced - wine_needed)
if wine_produced < wine_needed:
    print(f"It will be a tough winter! More {floor(wine_difference)} liters wine needed.")
else:
    print(f"Good harvest this year! Total wine: {floor(wine_produced)} liters.")
    print(f"{ceil(wine_difference)} liters left -> {ceil(wine_difference / workers)} liters per person.")