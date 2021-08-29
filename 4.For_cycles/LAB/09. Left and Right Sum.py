n = int(input())
sum_left = 0
for number in range(1, n + 1):
    value = int(input())
    sum_left += value

sum_right = 0
# value = 0
for number in range(n + 1, 2 * n + 1):
    value = int(input())
    sum_right += value

difference = abs(sum_left - sum_right)

if sum_left == sum_right:
    print(f"Yes, sum = {sum_left}")
else:
    print(f"No, diff = {difference}")
