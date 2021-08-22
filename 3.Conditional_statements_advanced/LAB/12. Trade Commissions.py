city = input()
sales = float(input())
commission = 0
# да сметна комисионната
if sales < 0:
    print("error")
elif city == "Sofia":
    if 0 <= sales <= 500:
        commission = .05 * sales
    elif 500 < sales <= 1000:
        commission = .07 * sales
    elif 1000 < sales <= 10000:
        commission = .08 * sales
    else:
        commission = .12 * sales
    print(f"{commission:.2f}")
elif city == "Varna":
    if 0 <= sales <= 500:
        commission = .045 * sales
    elif 500 < sales <= 1000:
        commission = .075 * sales
    elif 1000 < sales <= 10000:
        commission = .1 * sales
    else:
        commission = .13 * sales
    print(f"{commission:.2f}")
elif city == "Plovdiv":
    if 0 <= sales <= 500:
        commission = .055 * sales
    elif 500 < sales <= 1000:
        commission = .08 * sales
    elif 1000 < sales <= 10000:
        commission = .12 * sales
    else:
        commission = .145 * sales
    print(f"{commission:.2f}")
else:
    print("error")
