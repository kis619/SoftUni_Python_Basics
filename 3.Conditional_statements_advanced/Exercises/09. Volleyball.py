from math import floor
type_of_year = input()
holidays = p = int(input())
weekends_at_his_hometown = h = int(input())

volleyball_on_holidays = 2/3 * p

weekends_at_sofia = 48 - h
weekends_at_work = .25 * weekends_at_sofia

volleyball_during_the_weekend = weekends_at_sofia - weekends_at_work

days_volleyball = volleyball_on_holidays + volleyball_during_the_weekend + h

if type_of_year == "leap":
    days_volleyball *= .15 + 1

print(floor(days_volleyball))