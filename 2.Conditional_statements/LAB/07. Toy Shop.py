price_puzzle = 2.60
price_talking_doll = 3.00
price_teddy_bear = 4.10
price_minion = 8.20
price_little_truck = 2.00

vacation_price = float(input())
puzzles = int(input())
talking_dolls = int(input())
teddy_bears = int(input())
minions = int(input())
little_trucks = int(input())

number_ordered_toys = puzzles + talking_dolls + teddy_bears + minions + little_trucks

revenue = puzzles * price_puzzle + talking_dolls * price_talking_doll + \
          teddy_bears * price_teddy_bear + minions * price_minion + \
          little_trucks * price_little_truck
if number_ordered_toys >= 50:
    revenue = 0.75 * revenue        # 50+ играчки водят до 25% отстъпка

shop_rent = 0.1 * revenue
holiday_money = revenue - shop_rent
surplus = holiday_money - vacation_price
insufficient_resources = vacation_price - holiday_money
if holiday_money >= vacation_price:
    print(f"Yes! {surplus:.2f} lv left.")
    # print(f"Yes! {(holiday_money - vacation_price):.2f} lv left.")
else:
    print(f"Not enough money! {insufficient_resources:.2f} lv needed.")
    # print(f"Not enough money! {(vacation_price - holiday_money):.2f} lv needed.")
