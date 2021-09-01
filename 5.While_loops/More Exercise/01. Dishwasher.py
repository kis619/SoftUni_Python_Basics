# bottle = 750 ml
# dish = 5  ml
# pot = 15 ml

detergent = int(input())
enough_detergent = True
counter = 0
used_detergent = 0
clean_dishes = 0
clean_pots = 0

while enough_detergent:
    command = input()
    if command == "End":
        break
    counter += 1
    item = int(command)
    if counter % 3 != 0:
        used_detergent += item * 5
        clean_dishes += item
    else:
        used_detergent += item * 15
        clean_pots += item
    if used_detergent > detergent * 750:
        enough_detergent = False



if enough_detergent:
    print("Detergent was enough!")
    print(f"{clean_dishes} dishes and {clean_pots} pots were washed.")
    print(f"Leftover detergent {detergent * 750 - used_detergent} ml.")
else:
    print(f"Not enough detergent, {used_detergent - detergent * 750} ml. more necessary!")
