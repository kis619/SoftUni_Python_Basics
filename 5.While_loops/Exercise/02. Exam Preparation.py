number_failed_grades_allowed = int(input())
problem_name = input()


failed_grades = 0
sum_grades = 0
number_of_problems = 0
last_problem_name = ""
while problem_name != "Enough":
    grade = int(input())
    if grade <= 4:
        failed_grades += 1
        if number_failed_grades_allowed == failed_grades:
            print(f"You need a break, {failed_grades} poor grades.")
            break
    sum_grades += grade
    number_of_problems += 1
    last_problem_name = problem_name
    problem_name = input()
else:
    average_grade = sum_grades / number_of_problems
    print(f"Average score: {average_grade:.2f}")
    print(f"Number of problems: {number_of_problems}")
    print(f"Last problem: {last_problem_name}")