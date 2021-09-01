added_money = input()
sum = 0
while added_money != "NoMoreMoney":
    if float(added_money) < 0:
        print("Invalid operation!")
        break
    sum += float(added_money)
    print(f"Increase: {float(added_money):.2f}")
    added_money = input()


print(f"Total: {sum:.2f}")
