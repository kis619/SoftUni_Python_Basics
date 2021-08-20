from math import floor

record = float(input())
distance = float(input())
seconds_per_meter = float(input())

water_resistance = (floor(distance / 15) * 12.5)
ivan_time = distance * seconds_per_meter + water_resistance
old_record_faster = ivan_time - record
new_record_faster = record - ivan_time
if ivan_time < record:
    print(f"Yes, he succeeded! The new world record is {ivan_time:.2f} seconds.")
else:
    print(f"No, he failed! He was {old_record_faster:.2f} seconds slower.")
