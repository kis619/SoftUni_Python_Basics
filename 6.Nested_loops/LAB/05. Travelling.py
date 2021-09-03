destination = input()

while destination != "End":
    budget = float(input())
    saved_money = 0
    while saved_money < budget:
        money_added_to_savings = float(input())
        saved_money += money_added_to_savings
    else:
        print(f"Going to {destination}!")
        destination = input()

# Judge връща грешка за ред 24: ValueError: could not convert string to float
destination = input()
budget = float(input())
saved_money = 0
while destination != "End":
    money_input = float(input())
    saved_money += money_input
    if saved_money >= budget:
        print(f"Going to {destination}!")
        saved_money = 0
        destination = input()
        budget = float(input())

# Judge връща грешка за ред 24: ValueError: could not convert string to float
destination = input()
budget = float(input())
while destination != "End":
    saved_money = 0
    while saved_money < budget:
        money_added_to_savings = float(input())
        saved_money += money_added_to_savings
    else:
        print(f"Going to {destination}!")
        destination = input()
        budget = float(input())
