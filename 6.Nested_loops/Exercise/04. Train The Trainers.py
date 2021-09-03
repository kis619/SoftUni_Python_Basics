people_in_the_jury = int(input())

presentation_title = input()
number_of_presentations = 0
marks_all_presentations = 0
while presentation_title != "Finish":
    number_of_presentations += 1
    marks_single_presentation = 0
    for each_presentation in range(1, people_in_the_jury + 1):
        mark = float(input())
        marks_single_presentation += mark
    average_mark_single_presentation = marks_single_presentation / people_in_the_jury
    marks_all_presentations += average_mark_single_presentation
    print(f"{presentation_title} - {average_mark_single_presentation:.2f}.")
    presentation_title = input()

average_all_presentations = marks_all_presentations / number_of_presentations
print(f"Student's final assessment is {average_all_presentations:.2f}.")



