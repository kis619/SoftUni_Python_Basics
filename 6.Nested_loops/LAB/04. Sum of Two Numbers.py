first_number = int(input())
last_number = int(input())
magic_number = int(input())
combination_counter = 0
combination_equal_to_magic_number = False
for n1 in range(first_number, last_number + 1):
    for n2 in range(first_number, last_number + 1):
        sum = n1 + n2
        combination_counter += 1
        if sum == magic_number:
            combination_equal_to_magic_number = True
            break
    if sum == magic_number:
        break

if combination_equal_to_magic_number:
    print(f"Combination N:{combination_counter} ({n1} + {n2} = {magic_number})")
else:
    print(f"{combination_counter} combinations - neither equals {magic_number}")
