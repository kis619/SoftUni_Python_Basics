number_of_open_sites = int(input())
salary = float(input())
# facebook_fee = 150
# instagram_fee = 100
# reddit_fee = 50
for i in range(number_of_open_sites):
    site_name = input()
    if site_name == "Facebook":
        salary -= 150
    elif site_name == "Instagram":
        salary -= 100
    elif site_name == "Reddit":
        salary -= 50
    if salary <= 0:
        break

if salary <= 0:
    print("You have lost your salary.")
else:
    print(int(salary))