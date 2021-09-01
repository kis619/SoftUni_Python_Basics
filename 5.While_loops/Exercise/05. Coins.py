# Напишете програма, която приема сума - рестото, което трябва да се върне
# и изчислява с колко най-малко монети може да стане това.
change_in_leva = float(input())
change = change_in_leva * 100
number_of_coins = 0
while change != 0:
    if change >= 200:
        number_of_coins += change // 200
        change -= 200 * (change // 200)
    elif change >= 100:
        number_of_coins += change // 100
        change -= 100 * (change // 100)
    elif change >= 50:
        number_of_coins += change // 50
        change -= 50 * (change // 50)
    elif change >= 20:
        number_of_coins += change // 20
        change -= 20 * (change // 20)
    elif change >= 10:
        number_of_coins += change // 10
        change -= 10 * (change // 10)
    elif change >= 5:
        number_of_coins += change // 5
        change -= 5 * (change // 5)
    elif change >= 2:
        number_of_coins += change // 2
        change -= 2 * (change // 2)
    elif change >= 1:
        number_of_coins += 1
        break



print(int(number_of_coins))




