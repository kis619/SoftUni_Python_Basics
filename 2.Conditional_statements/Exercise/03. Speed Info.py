speed = float(input())
information_about_speed = str
if speed <= 10:
    information_about_speed = str("slow")
elif speed > 10 and speed <= 50: # 10 < speed <= 50
    information_about_speed = str("average")
elif speed > 50 and speed <= 150:
    information_about_speed = str("fast")
elif speed > 150 and speed <= 1000:
    information_about_speed = str("ultra fast")
elif speed > 1000:
    information_about_speed = str("extremely fast")

print(information_about_speed)