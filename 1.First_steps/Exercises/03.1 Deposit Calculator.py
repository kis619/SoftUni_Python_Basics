deposited_sum = float(input())
months = int(input())
yearly_interest_rate = float(input())
money_YIR = deposited_sum * yearly_interest_rate / 100  # YIR = yearly interest rate
money_MIR = money_YIR / 12  # MIR = monthly interest rate
total_interest_rate = money_MIR * months
total_sum = deposited_sum + total_interest_rate
print(total_sum)
