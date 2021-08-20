from math import ceil
from math import floor
days = int(input())
food_she_left = int(input())
food_dog_day = float(input())
food_cat_day = float(input())
food_turtle_day = float(input()) # в грамове щото що не

food_dog_needs = days * food_dog_day
food_cat_needs = days * food_cat_day
food_turtle_needs = days * food_turtle_day * .001
food_needed = food_turtle_needs + food_cat_needs + food_dog_needs

difference = abs(food_needed - food_she_left)

if food_needed > food_she_left:
    print(f"{ceil(difference)} more kilos of food are needed.")
else:
    print(f"{floor(difference)} kilos of food left.")