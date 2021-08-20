kilometer = int(input())
time_of_day = input()

taxi_price = 0
train_ticket = kilometer * .06
bus_fare = kilometer * .09
if time_of_day == "day":
    taxi_price = .7 + kilometer * .79
else:
    taxi_price = .7 + kilometer * .9

if kilometer < 20:
    print(f"{taxi_price:.2f}")

elif 100 > kilometer >= 20:
    if taxi_price > bus_fare:
        print(f"{bus_fare:.2f}")
    else:
        print(f"{taxi_price:.2f}")

else:
    if train_ticket > bus_fare > taxi_price:
        print(f"{taxi_price:.2f}")
    elif train_ticket > bus_fare < taxi_price:
        print(f"{bus_fare:.2f}")
    elif train_ticket < bus_fare < taxi_price:
        print(f"{train_ticket:.2f}")
    elif train_ticket < taxi_price < bus_fare:
        print(f"{train_ticket:.2f}")
    elif taxi_price > train_ticket > bus_fare:
        print(f"{bus_fare:.2f}")
    else:
        print(f"{taxi_price:.2f}")

