number = int(input())

for special_number in range(1111, 10000):
    it_is_special = True
    special_number_str = str(special_number)
    for digit in special_number_str:
        if int(digit) == 0 or number % int(digit) != 0:
            it_is_special = False
            break
    if it_is_special:
        print(special_number, end=" ")