# flower_m = 3.25
# flower_z = 4
# flower_r = 3.5
# flower_c = 8

from math import ceil
from math import floor

number_m = int(input())
number_z = int(input())
number_r = int(input())
number_c = int(input())
gift_price = float(input())
revenue = number_m * 3.25 + number_z * 4 \
    + number_r * 3.5 + number_c * 8
# 5% tax
revenue *= .95
difference = abs(gift_price - revenue)

if revenue >= gift_price:
    print(f"She is left with {floor(difference)} leva.")
else:
    print(f"She will have to borrow {ceil(difference)} leva.")
