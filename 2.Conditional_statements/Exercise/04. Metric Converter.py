number = float(input())
in_unit = input()
out_unit = input()

if in_unit == str("m") and out_unit == str("cm"):
    result = number * 100
elif in_unit == str("cm") and out_unit == str("m"):
    result = number / 100
elif in_unit == str("m") and out_unit == str("mm"):
    result = number * 1000
elif in_unit == str("mm") and out_unit == str("m"):
    result = number / 1000
elif in_unit == str("cm") and out_unit == str("mm"):
    result = number * 10
elif in_unit == str("mm") and out_unit == str("cm"):
    result = number / 10
print(f"{result:.3f}")