# тук е вярно, в джъдж гърми


flower = input()
number_of_flowers = int(input())
budget = int(input())

flower_price = 0
price = flower_price * number_of_flowers
discount = 0
if flower == "Roses":
    flower_price = 5
    if number_of_flowers > 80:
        discount = 0.1 * price
    price -= discount
elif flower == "Dahlias":
    flower_price = 3.8
    if number_of_flowers > 90:
        discount = 0.15 * price
    price -= discount
elif flower == "Tulips":
    flower_price = 2.80
    if number_of_flowers > 80:
        discount = .15 * price
    price -= discount
elif flower == "Narcissus":
    flower_price = 3
    if number_of_flowers < 120:
        additional_amount = .15 * price
    price += additional_amount
elif flower == "Gladiolus":
    flower_price = 2.5
    if number_of_flowers < 80:
        additional_amount = .2 * price
    price += additional_amount

money_difference = abs(budget - price)

if budget >= price:
    print(f"Hey, you have a great garden with {number_of_flowers} {flower} and {money_difference:.2f} leva left.")
else:
    print(f"Not enough money, you need {money_difference:.2f} leva more.")
