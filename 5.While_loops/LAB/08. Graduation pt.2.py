# само дето тази трябваше да се реши с while

name = input()
sum_grades = 0
poor_marks = 0
poor_mark = 0
for i in range(1, 13):
    grade = float(input())
    if i == 0 and grade >= 4:
        sum_grades+= grade
    elif i == 0 and grade <4:
        poor_marks += 1
    if grade >= 4:
        sum_grades += grade
    else:
        poor_marks += 1
        poor_mark = grade
    if poor_marks >= 2:
        print(f"{name} has been excluded at {i-1} grade")
        break
if poor_marks == 0:
    print(f"{name} graduated. Average grade: {sum_grades/12:.2f}")
elif poor_marks < 2:
    print(f"{name} graduated. Average grade: {sum_grades - poor_mark/12:.2f}")


