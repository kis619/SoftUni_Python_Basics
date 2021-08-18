deposited_sum = float(input())
number_of_months = int(input())
yearly_interest_rate = float(input())
final_sum = deposited_sum + yearly_interest_rate / 100 * deposited_sum / 12 * number_of_months
print(final_sum)
