time1 = int(input())
time2 = int(input())
time3 = int(input())

total = time3 + time2 + time1

minutes = total // 60
seconds = total % 60
if seconds < 10:
    seconds = f"0{seconds}"

print(f"{minutes}:{seconds}")
