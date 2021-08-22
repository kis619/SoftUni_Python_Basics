days = int(input())
room = input()
feedback = input()

room_for_one_person_per_night = 18.00
apartment_per_night = 25.00
president_apartment = 35.00
nights = days - 1
discount = 0

if room == "room for one person":
    expenses = room_for_one_person_per_night * nights
    if feedback == "positive":
        final_price = 1.25 * expenses
    elif feedback == "negative":
        final_price = 0.9 * expenses
    print(f"{final_price:.2f}")
elif room == "apartment":
    expenses = 25 * nights
    if days < 10:
        discount = expenses * 0.3
    elif 10 <= days <= 15:
        discount = expenses * 0.35
    else:
        discount = expenses * .5
    price_after_discount = expenses - discount
    if feedback == "positive":
        final_price = 1.25 * price_after_discount
    elif feedback == "negative":
        final_price = .9 * price_after_discount
    print(f"{final_price:.2f}")

elif room == "president apartment":
    expenses = 35 * nights
    if days < 10:
        discount = expenses * 0.1
    elif 10 <= days <= 15:
        discount = expenses * 0.15
    else:
        discount = expenses * .2
    price_after_discount = expenses - discount
    if feedback == "positive":
        final_price = 1.25 * price_after_discount
    elif feedback == "negative":
        final_price = .9 * price_after_discount
    print(f"{final_price:.2f}")