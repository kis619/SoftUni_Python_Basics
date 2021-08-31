import sys

text = input()
max_number = -sys.maxsize
while text != "Stop":
    if int(text) > max_number:
        max_number = int(text)
    text = input()
print(max_number)