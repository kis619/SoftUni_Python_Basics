# roses = 5
# dahlias = 3.80
# tulips = 2.30
# narcissus = 3
# gladiolus = 2.50
flower = input()
number_of_flowers = int(input())
budget = int(input())

flower_price = 0
if flower == "Roses":
    flower_price = 5
elif flower == "Dahlias":
    flower_price = 3.8
elif flower == "Tulips":
    flower_price = 2.80
elif flower == "Narcissus":
    flower_price = 3
elif flower == "Gladiolus":
    flower_price = 2.5

price = flower_price * number_of_flowers

if flower == "Roses" and number_of_flowers > 80:
    discount = 0.1 * price
    price -= discount
elif flower == "Dahlias" and number_of_flowers > 90:
    discount = 0.15 * price
    price -= discount
elif flower == "Tulips" and number_of_flowers > 80:
    discount = .15 * price
    price -= discount
elif flower == "Narcissus" and number_of_flowers < 120:
    additional_amount = .15 * price
    price += additional_amount
elif flower == "Gladiolus" and number_of_flowers < 80:
    additional_amount = .2 * price
    price += additional_amount

money_difference = abs(budget - price)
if budget >= price:
    print(f"Hey, you have a great garden with {number_of_flowers} {flower} and {money_difference:.2f} leva left.")
else:
    print(f"Not enough money, you need {money_difference:.2f} leva more.")
