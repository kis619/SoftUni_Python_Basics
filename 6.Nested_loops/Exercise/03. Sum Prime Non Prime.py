command = input()
sum_prime_numbers = 0
sum_non_prime_numbers = 0

while command != "stop":
    number = int(command)
    is_a_prime_number = True
    if number < 0:
        print("Number is negative.")
        command = input()
        continue
    for divisor in range(2, 10):
        if number % divisor == 0 and number != divisor:
            is_a_prime_number = False
            sum_non_prime_numbers += number
            break
    if is_a_prime_number:
        sum_prime_numbers += number
    command = input()

print(f"Sum of all prime numbers is: {sum_prime_numbers}")
print(f"Sum of all non prime numbers is: {sum_non_prime_numbers}")