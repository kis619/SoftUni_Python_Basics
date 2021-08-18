vegetable_price = float(input())
fruit_price = float(input())
vegetables = int(input())
fruit = int(input())

lv = vegetables * vegetable_price + fruit * fruit_price
lv_to_eur = lv / 1.94
print(f"{lv_to_eur:.2f}")
