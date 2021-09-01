name = input()
poor_marks = 0
poor_mark = 0
grade = 1
sum_marks = 0
while grade < 13:
    mark = float(input())
    if mark >= 4:
        grade += 1
        sum_marks += mark
    else:
        poor_marks += 1
        poor_mark = mark
        if poor_marks == 2:
            print(f"{name} has been excluded at {grade} grade")
            break
if poor_marks < 2:
    print(f"{name} graduated. Average grade: {(sum_marks - poor_mark) / 12:.2f}")