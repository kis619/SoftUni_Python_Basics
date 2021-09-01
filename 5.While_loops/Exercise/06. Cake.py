cake_width = int(input())
cake_length = int(input())

cake_area = cake_length * cake_width
total_pieces = 0

while cake_area > 0:
    command = input()
    if command != "STOP":
        number_of_pieces = int(command)
        total_pieces += number_of_pieces
        cake_area -= number_of_pieces
    else:
        print(f"{cake_area} pieces are left.")
        break

else:
    print(f"No more cake left! You need {total_pieces - (cake_width * cake_length)} pieces more.")

