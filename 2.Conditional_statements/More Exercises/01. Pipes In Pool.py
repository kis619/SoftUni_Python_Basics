v = int(input())
p1 = int(input())
p2 = int(input())
h = float(input())

p1_debit = p1 * h
p2_debit = p2 * h
occupied_volume = p1_debit + p2_debit
occupied_volume_percent = occupied_volume / v * 100

if occupied_volume <= v:
    print(f"The pool is {occupied_volume_percent}% full. Pipe 1: {p1_debit / occupied_volume * 100:.2f}%.\
     Pipe 2: {p2_debit / occupied_volume * 100:.2f}%.")
else:
    print(f"For {h} hours the pool overflows with {occupied_volume - v:.2f} liters.")
