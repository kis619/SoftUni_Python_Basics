# тъпа задача, ен ми се занимава


w = float(input())
h = float(input())

area = w * h

unit = .7 * 1.2
door = 1 * unit
desk = 2 * unit
corridor = w * 1
free_area = area - door - desk - corridor
number_of_units = free_area // unit
print(int(number_of_units))