age = int(input())
washing_machine = float(input())
toy_price = int(input())

saved_money = 0
received_money = 0

for birthday in range(1, age + 1):
    if birthday % 2 != 0:
        saved_money += toy_price
    elif birthday % 2 == 0 and birthday == 2:
        received_money = 10
        saved_money += received_money
    elif birthday % 2 == 0 and birthday != 2:
        received_money += 10
        saved_money += received_money

saved_money -= age//2
difference = abs(washing_machine - saved_money)

if saved_money >= washing_machine:
    print(f"Yes! {difference:.2f}")
else:
    print(f"No! {difference:.2f}")