roses = 5
dahlias = 3.80
tulips = 2.30
narcissus = 3
gladiolus = 2.50

flower = input()
number_of_flowers = int(input())
budget = int(input())
if flower == "Roses":
    final_price = number_of_flowers * 5
elif flower == "Dahlias":
    final_price = number_of_flowers * 3.8
elif flower == "Tulips":
    final_price = number_of_flowers * 2.80
elif flower == "Narcissus":
    final_price = number_of_flowers * 3
elif flower == "Gladiolus":
    final_price = number_of_flowers * 2.5

if flower == "Roses" and number_of_flowers > 80:
    price = number_of_flowers * 5
    discount = 0.1 * price
    final_price = price - discount
elif flower == "Dahlias" and number_of_flowers > 90:
    price = number_of_flowers * 3.8
    discount = 0.15 * price
    final_price = price - discount
elif flower == "Tulips" and number_of_flowers > 80:
    price = number_of_flowers * 2.80
    discount = .15 * price
    final_price = price - discount
elif flower == "Narcissus" and number_of_flowers < 120:
    price = number_of_flowers * 3
    additional_amount = .15 * price
    final_price = price + additional_amount
elif flower == "Gladiolus" and number_of_flowers < 80:
    price = number_of_flowers * 2.5
    additional_amount = .2 * price
    final_price = price + additional_amount

money_difference = abs(budget - final_price)
if budget >= final_price:
    print(f"Hey, you have a great garden with {number_of_flowers} {flower} and {money_difference:.2f} leva left.")
else:
    print(f"Not enough money, you need {money_difference:.2f} leva more.")
