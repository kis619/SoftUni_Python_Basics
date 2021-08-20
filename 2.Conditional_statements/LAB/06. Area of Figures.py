from math import pow
from math import pi

shape = input()
if shape == "square":
    a = float(input())
    area = pow(a, 2)
    # square_area = f"{square_area:.3F}"
    # print(square_area)
    print(f"{area:.3f}")
elif shape == "rectangle":
    a = float(input())
    b = float(input())
    area = a * b
    print(f"{area:.3f}")
elif shape == "circle":
    r = float(input())
    area = pi * pow(r, 2)
    print(f"{area:.3f}")
elif shape == "triangle":
    a = float(input())
    ha = float(input())
    area = a * ha / 2
    print(f"{area:.3f}")
