book_needed = input()
book_name = input()
books_checked = 0
while book_name != book_needed:
    if book_name == "No More Books":
        print(f"The book you search is not here!")
        print(f"You checked {books_checked} books.")
        break
    book_name = input()
    books_checked += 1


else:
    print(f"You checked {books_checked} books and found it.")
