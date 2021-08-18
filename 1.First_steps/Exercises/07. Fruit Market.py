strawberries_price = float(input())
raspberries_price = strawberries_price / 2
oranges_price = raspberries_price * 0.60
bananas_price = raspberries_price * .20

bananas = float(input())
oranges = float(input())
raspberries = float(input())
strawberries = float(input())

raspberries_sum = raspberries * raspberries_price
strawberries_sum = strawberries * strawberries_price
bananas_sum = bananas * bananas_price
oranges_sum = oranges * oranges_price

sum_total = strawberries_sum + oranges_sum + raspberries_sum + bananas_sum
print(sum_total)

