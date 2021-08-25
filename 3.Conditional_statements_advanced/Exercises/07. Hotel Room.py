month = input()
nights = int(input())
studio_price = 0
apartment_price = 0
discount_studio = 0
discount_apartment = 0

if month == "May" or month == "October":
    studio_price = 50
    apartment_price = 65
    if nights > 7 and nights < 14:
        discount_studio = .05 * studio_price * nights
    elif nights > 14:
        discount_studio = .3 * studio_price * nights
elif month == "June" or month == "September":
    studio_price = 75.20
    apartment_price = 68.70
    if nights > 14:
        discount_studio = .2 * studio_price * nights
else:
    studio_price = 76
    apartment_price = 77

if nights > 14:
    discount_apartment = .1 * apartment_price * nights

expenses_studio = studio_price * nights - discount_studio
expenses_apartment = apartment_price * nights - discount_apartment

print(f"Apartment: {expenses_apartment:.2f} lv.")
print(f"Studio: {expenses_studio:.2f} lv.")

