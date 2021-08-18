days = int(input())
bakers = int(input())
cakes = int(input())
waffles = int(input())
crepes = int(input())
cake_price = 45
waffle_price = 5.80
crepes_price = 3.20
sum_cakes = cakes * cake_price
sum_waffles = waffles * waffle_price
sum_crepes = crepes * crepes_price
sum_1_day = sum_crepes + sum_cakes + sum_waffles
sum_total = sum_1_day * days * bakers
spendings = sum_total / 8
collected_money = sum_total - spendings
print(collected_money)
