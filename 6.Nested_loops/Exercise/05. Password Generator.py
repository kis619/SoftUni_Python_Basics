number_1 = int(input())
number_2 = int(input())

for symbol1 in range(1, number_1 + 1):
    for symbol2 in range(1, number_1 + 1):
        for symbol3 in range(97, number_2 + 97):
            for symbol4 in range(97, number_2 + 97):
                for symbol5 in range(1, number_1 + 1):

                    if symbol5 > symbol1 and symbol5 > symbol2:
                        print(f"{symbol1}{symbol2}{chr(symbol3)}{chr(symbol4)}{symbol5}", end= " ")

# 97 122

