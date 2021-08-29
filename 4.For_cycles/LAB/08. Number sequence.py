import sys

n = int(input())
max_number = -sys.maxsize
min_number = sys.maxsize
for number in range(0, n): #(1, n + 1)
    value = int(input())
    if value > max_number:
        max_number = value
    if value < min_number:
        min_number = value



print(f"Max number: {max_number}")
print(f"Min number: {min_number}")

