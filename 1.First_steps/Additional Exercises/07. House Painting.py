import math
x = float(input())
y = float(input())
h = float(input())

front_and_back = 2 * math.pow(x, 2) - 1.2 * 2
sides = 2 * x * y - 2 * math.pow(1.5, 2)
roof_front = x * h /2 * 2
roof_side = x * y * 2

# 1l zelena boq = 3.4m2
# 1 / 3.42
paint_walls = (front_and_back + sides) / 3.4
paint_roof = (roof_side + roof_front) / 4.3

print(f"{paint_walls:.2f}")
print(f"{paint_roof:.2f}")