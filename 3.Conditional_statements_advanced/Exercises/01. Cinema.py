type_of_film = input()
r = int(input())
c = int(input())

premiere = 12.00
normal = 7.5
discount = 5

# revenue = 0
if type_of_film == "Premiere":
    revenue = r * c * premiere
elif type_of_film == "Normal":
    revenue = r * c * normal
else:
    revenue = r * c * discount

print(f"{revenue:.2f} leva")

