word = input()

counter_c = 0
counter_o = 0
counter_n = 0
searched = ""
words_to_print = ""
while word != "End":
    if 65 <= ord(word) <= 90 or 97 <= ord(word) <= 122: # 65 do 90 and 97 do 122
        if word == "c":
            counter_c += 1
            if counter_c > 1:
                searched += word
        elif word == "o":
            counter_o += 1
            if counter_o > 1:
                searched += word
        elif word == "n":
            counter_n += 1
            if counter_n > 1:
                searched += word
        else:
            searched += word
        if counter_n > 0 and counter_c > 0 and counter_o > 0:
            searched += " "
            words_to_print = searched
            counter_c = 0
            counter_o = 0
            counter_n = 0

    word = input()

print(words_to_print)

