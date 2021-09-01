# Напишете програма, която приема сума - рестото, което трябва да се върне
# и изчислява с колко най-малко монети може да стане това.
# 2.30 не излиза
change_in_leva = float(input())
change = int(change_in_leva * 100)
number_of_coins = 0


number_of_coins += change // 200
change %= 200 # change % 200 368 : 200 = 1

number_of_coins += change // 100
change %= 100

number_of_coins += change // 50
change %= 50

number_of_coins += change // 20
change %= 20

number_of_coins += change // 10
change %= 10

number_of_coins += change // 5
change %= 5

number_of_coins += change // 2
change %= 2

number_of_coins += change // 1
change %= 1




print(number_of_coins)




