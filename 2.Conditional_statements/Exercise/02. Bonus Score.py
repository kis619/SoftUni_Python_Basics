number = int(input())
first_bonus = 0
second_bonus = 0
third_bonus = 0


if number <= 100:
    first_bonus = 5

elif number > 1000:
    first_bonus = 0.1 * number

else:
    first_bonus = 0.2 * number

if number % 2 == 0:
    second_bonus = 1

if number % 5 == 0 and number % 2 != 0:
    third_bonus = 2

all_bonuses = first_bonus + second_bonus + third_bonus
new_number = number + all_bonuses
print(all_bonuses)
print(new_number)
