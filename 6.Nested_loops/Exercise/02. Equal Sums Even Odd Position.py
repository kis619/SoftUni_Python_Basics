# first_number = input()
# second_number = input()
#
# first_digit = first_number[0]
# third_digit = first_number[2]
# fifth_digit = first_number[4]
# second_digit = first_number[1]
# fourth_digit = first_number[3]
# sixth_digit = first_number[5]
# odd_sum_first_number = int(first_digit) + int(third_digit) + int(fifth_digit)
# even_sum_first_number = int(second_digit) + int(fourth_digit) + int(sixth_digit)

# first_digit_second_number = second_number[0]
# third_digit_second_number = second_number[2]
# fifth_digit_second_number = second_number[4]
# second_digit_second_number = second_number[1]
# fourth_digit_second_number = second_number[3]
# sixth_digit_second_number = second_number[5]
#
# odd_sum_second_number = int(first_digit_second_number) + int(third_digit_second_number) + int(fifth_digit_second_number)
# even_sum_second_number = int(second_digit_second_number) + int(fourth_digit_second_number) + int(sixth_digit_second_number)

# first_number_int = int(first_number)
# second_number_int = int(second_number)
first_number = int(input())
second_number = int(input())
for number in range(first_number, second_number+ 1):
    value = str(number)
    first_digit = value[0]
    third_digit = value[2]
    fifth_digit = value[4]
    second_digit = value[1]
    fourth_digit = value[3]
    sixth_digit = value[5]
    odd_sum_first_number = int(first_digit) + int(third_digit) + int(fifth_digit)
    even_sum_first_number = int(second_digit) + int(fourth_digit) + int(sixth_digit)
    if odd_sum_first_number == even_sum_first_number:
        print(number, end= " ")
    # if odd_sum_second_number == even_sum_second_number:
    #     print(number, end= " ")
