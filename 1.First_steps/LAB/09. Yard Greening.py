# needed_resources
# 18% discount of final price
price_one_sqr_m = 7.61
sqr_m = float(input())
price_without_discount = price_one_sqr_m * sqr_m
discount = 18/100 * price_without_discount
needed_resources = price_without_discount - discount
# needed_resources = 0.82 * price_without_discount дава 3432.109999999
print(f"The final price is: {needed_resources} lv.")
print(f"The discount is: {discount} lv.")
