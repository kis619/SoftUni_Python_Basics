exam_hour = int(input())
exam_minutes = int(input())
arrival_hour = int(input())
arrival_minutes = int(input())

exam_hour_to_minutes = exam_hour * 60
arrival_hour_to_minutes = arrival_hour * 60

exam_time_in_minutes = exam_hour_to_minutes + exam_minutes
arrival_time_in_minutes = arrival_hour_to_minutes + arrival_minutes

if arrival_time_in_minutes > exam_time_in_minutes:
    print("Late")
elif arrival_time_in_minutes == exam_time_in_minutes or arrival_time_in_minutes >= exam_time_in_minutes - 30:
    print("On time")
else:
    print("Early")

difference = abs(arrival_time_in_minutes - exam_time_in_minutes)
hours = difference // 60
minutes = difference % 60

if exam_time_in_minutes - 60 < arrival_time_in_minutes < exam_time_in_minutes:
    print(f"{difference} minutes before the start")
elif arrival_time_in_minutes <= exam_time_in_minutes - 60:
    print(f"{hours}:{minutes:0>2d} hours before the start")
elif exam_time_in_minutes + 60 > arrival_time_in_minutes > exam_time_in_minutes:
    print(f"{difference} minutes after the start")
elif arrival_time_in_minutes >= exam_time_in_minutes + 60:
    print(f"{hours}:{minutes:0>2d} hours after the start")