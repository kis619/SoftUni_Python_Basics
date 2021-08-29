number_of_open_sites = int(input())
salary = float(input())
# facebook_fee = 150
# instagram_fee = 100
# reddit_fee = 50
fee = 0
for i in range(number_of_open_sites):
    site_name = str(input())
    if site_name == "Facebook":
        fee += 150
    elif site_name == "Instagram":
        fee += 100
    elif site_name == "Reddit":
        fee += 50
    if fee >= salary: # salary <= 0
        break

if fee >= salary:
    print("You have lost your salary.")
else:
    print(int(salary - fee))