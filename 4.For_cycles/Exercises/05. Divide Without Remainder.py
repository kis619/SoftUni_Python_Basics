n = int(input())
p2 = 0
p3 = 0
p4 = 0

for number in range(1, n + 1):
    value = int(input())
    if value % 2 == 0:
        p2 += 1
    if value % 3 == 0:
        p3 += 1
    if value % 4 == 0:
        p4 += 1

percent_p2 = p2 / n * 100
percent_p3 = p3 / n * 100
percent_p4 = p4 / n * 100

print(f"{percent_p2:.2f}%")
print(f"{percent_p3:.2f}%")
print(f"{percent_p4:.2f}%")