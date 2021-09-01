# тук работи, но джъдж дава run time error: EOF when reading a line grade = float(input())
number_of_poor_grades_allowed = int(input())
poor_grades = 0
number_of_problems = 0
sum_grades = 0
last_problem_name = "a"
while poor_grades < number_of_poor_grades_allowed:
    problem_name = input()
    if problem_name != "Enough":
        last_problem_name = problem_name
        grade = float(input())
        if grade <= 4:
            poor_grades += 1
        number_of_problems += 1
        sum_grades += grade
    else:
        print(f"Average score: {sum_grades / number_of_problems:.2f}")
        print(f"Number of problems: {number_of_problems}")
        print(f"Last problem: {last_problem_name}")


print(f"You need a break, {poor_grades} poor grades.")