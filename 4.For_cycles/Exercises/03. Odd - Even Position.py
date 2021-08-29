import sys

n = int(input())
even_max = -sys.maxsize
even_min = sys.maxsize
odd_max = -sys.maxsize
odd_min = sys.maxsize
even_sum = 0
odd_sum = 0

# чете числата
# четна или нечетна позиция
# if четна, намери SUM, MAX and MIN от четни
# if нечетна, намери SUM, MAX and MIN от нечетни
# ако няма min/max елемент ==> "No"

for i in range (1, n + 1):
    value = float(input())
    if not i % 2 == 0:
        odd_sum += value
        if value < odd_min:
            odd_min = value
        if value > odd_max:
            odd_max = value
    else:
        even_sum += value
        if value < even_min:
            even_min = value
        if value > even_max:
            even_max = value

print(f"OddSum={odd_sum:.2f},")

if n != 0:
    print(f"OddMin={odd_min:.2f},")
    print(f"OddMax={odd_max:.2f},")
else:
    print(f"OddMin=No,")
    print(f"OddMax=No,")

print(f"EvenSum={even_sum:.2f},")

if n != 0 and n != 1:
    print(f"EvenMin={even_min:.2f},")
    print(f"EvenMax={even_max:.2f}")
else:
    print(f"EvenMin=No,")
    print(f"EvenMax=No")