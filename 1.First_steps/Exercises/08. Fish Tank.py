length = int(input())
width = int(input())
height = int(input())
occupied_volume = float(input()) / 100
volume = length * width * height
water_volume_cm3 = volume - occupied_volume * volume
water_volume_dm3 = water_volume_cm3 * 0.001
# 1см = 0,1дм 1см/10 = 0.1 дм
# см --> дм  /10
print(water_volume_dm3)
