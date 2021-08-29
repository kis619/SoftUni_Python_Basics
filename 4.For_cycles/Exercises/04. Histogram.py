n = int(input())

p1 = 0
p2 = 0
p3 = 0
p4 = 0
p5 = 0

for numbers in range(1, n +1):
    value = int(input())
    if value < 200:
        p1 += 1
    elif value < 400:
        p2 += 1
    elif value < 600:
        p3 += 1
    elif value < 800:
        p4 += 1
    else:
        p5 += 1

# all = p1 + p2 + p3 + p4 + p5
percent_p1 = p1 * 100 / n # all
percent_p2 = p2 * 100 / n # all
percent_p3 = p3 * 100 / n # all
percent_p4 = p4 * 100 / n # all
percent_p5 = p5 * 100 / n # all

print(f"{percent_p1:.2f}%")
print(f"{percent_p2:.2f}%")
print(f"{percent_p3:.2f}%")
print(f"{percent_p4:.2f}%")
print(f"{percent_p5:.2f}%")


#
# # на колко процента от