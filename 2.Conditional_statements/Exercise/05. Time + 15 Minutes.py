hours = int(input())
minutes = int(input())

hours_to_minutes = hours * 60
fifteen_minutes_later = hours_to_minutes + minutes + 15
new_hours = fifteen_minutes_later // 60
new_minutes = fifteen_minutes_later % 60

if new_hours == 24:
    new_hours = 0
if new_minutes < 10:
    new_minutes = f"0{new_minutes}"
# if new_minutes == 60:    - not wrong but appears unnecessary, just gotta figure out why
  #  new_minutes = 59
  #  new_hours = new_hours + 1
print(f"{new_hours}:{new_minutes}")


