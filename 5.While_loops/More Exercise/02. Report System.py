goal = int(input())

counter = 0
collected_money = 0
cash_payments = 0
cash = 0
card_payments = 0
card = 0

command = input()
while command != "End":
    item_price = int(command)
    counter += 1
    if counter % 2 != 0:
        if item_price > 100:
            print("Error in transaction!")
        else:
            print("Product sold!")
            collected_money += item_price
            cash += item_price
            cash_payments += 1
    else:
        if item_price < 10:
            print("Error in transaction!")
        else:
            print("Product sold!")
            collected_money += item_price
            card += item_price
            card_payments += 1
    if collected_money >= goal:
        print(f"Average CS: {cash/cash_payments:.2f}")
        print(f"Average CC: {card/card_payments:.2f}")
        break
    command = input()

else:
    print("Failed to collect required money for charity.")