import sys

n = int(input())
max_number = -sys.maxsize
sum = 0
for number in range(n):
    value = int(input())
    sum += value
    if value > max_number:
        max_number = value
sum_without_max_number = sum - max_number
difference_between_max_and_rest = abs(max_number - sum_without_max_number)
if sum_without_max_number == max_number:
    print("Yes")
    print(f"Sum = {sum_without_max_number}")
else:
    print("No")
    print(f"Diff = {difference_between_max_and_rest}")