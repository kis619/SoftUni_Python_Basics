film_title = input()
ticket_counter_all = 0
student_ticket_counter = 0
standard_ticket_counter = 0
kids_ticket_counter = 0
while film_title != "Finish":
    free_seats = int(input())
    type_of_ticket = input()
    ticket_counter_current_film = 0
    while type_of_ticket != "End":
        ticket_counter_current_film += 1
        ticket_counter_all += 1
        if type_of_ticket == "student":
            student_ticket_counter += 1
        elif type_of_ticket == "standard":
            standard_ticket_counter += 1
        elif type_of_ticket == "kid":
            kids_ticket_counter += 1
        if ticket_counter_current_film == free_seats:
            break
        type_of_ticket = input()
    occupied_seats = ticket_counter_current_film / free_seats * 100
    print(f"{film_title} - {occupied_seats:.2f}% full.")
    film_title = input()


print(f"Total tickets: {ticket_counter_all}")
print(f"{student_ticket_counter / ticket_counter_all * 100:.2f}% student tickets.")
print(f"{standard_ticket_counter / ticket_counter_all * 100:.2f}% standard tickets.")
print(f"{kids_ticket_counter/ticket_counter_all * 100:.2f}% kids tickets.")



