days_off = int(input())
work_days = 365 - days_off

# work days 63 minutes per day
# days off 127 minutes per day
playtime = days_off * 127 + work_days * 63
# good sleep <= 30 000 playtime
difference = abs(playtime - 30000)
hours = difference // 60
minutes = difference % 60
if playtime > 30000:
    print("Tom will run away")
    if minutes < 10:
        print(f"{hours} hours and 0{minutes} minutes more for play")
    else:
        print(f"{hours} hours and {minutes} minutes more for play")
else:
    print("Tom sleeps well")
    if minutes < 10:
        print(f"{hours} hours and 0{minutes} minutes less for play")
    else:
        print(f"{hours} hours and {minutes} minutes less for play")