width = int(input())
length = int(input())
height = int(input())

text = input()
space = width * length * height
occupied_space = 0
while text != "Done":
    number_of_boxes = int(text) #each box = 1cm3
    occupied_space += number_of_boxes
    if occupied_space > space:
        print(f"No more free space! You need {occupied_space - space} Cubic meters more.")
        break
    text = input()

if occupied_space < space:
    print(f"{space - occupied_space} Cubic meters left.")