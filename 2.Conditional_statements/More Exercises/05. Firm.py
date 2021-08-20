import math
needed_hours = int(input())
days_the_company_has = int(input())
workers = int(input())

trainings = 10 / 100 * days_the_company_has
overtime = workers * 2 * days_the_company_has / 8
days_the_company_has = days_the_company_has + overtime - trainings
overall_time = days_the_company_has * 8


difference = abs(math.floor(overall_time) - needed_hours)

if needed_hours > overall_time:
    print(f"Not enough time!{difference} hours needed.")
else:
    print(f"Yes!{difference} hours left.")