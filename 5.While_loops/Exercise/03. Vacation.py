needed_money = float(input())
money_she_has = float(input())

number_of_action_spend_in_a_row = 0
days = 0
while needed_money > money_she_has:
    action = input()  # spend or save
    amount = float(input())
    days += 1
    if action == "spend":
        number_of_action_spend_in_a_row += 1
        if money_she_has < amount:
            money_she_has = 0
        else:
            money_she_has -= amount

    else:
        number_of_action_spend_in_a_row = 0
        money_she_has += amount
    if number_of_action_spend_in_a_row == 5:
        print("You can't save the money.")
        print(days)
        break

else:
    print(f"You saved the money for {days} days.")