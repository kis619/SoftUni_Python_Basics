from math import floor

income = float(input())
average_grades = float(input())
minimal_wage = float(input())

social_scholarship = .35 * minimal_wage
scholar_results = average_grades * 25

requirements_not_met = income > minimal_wage or average_grades < 4.50 and average_grades < 5.50
requirements_social_scholarship_only_met = income < minimal_wage and average_grades > 4.50 and average_grades < 5.50
requirements_scholar_results_only_met = income > minimal_wage and average_grades > 5.50
requirements_met_both = income < minimal_wage and average_grades > 5.50

if requirements_not_met:
    print("You cannot get a scholarship!")

elif requirements_social_scholarship_only_met:
    print(f"You get a scholarship {floor(social_scholarship)} BGN")

elif requirements_scholar_results_only_met:
    print(f"You get a scholarship for excellent results {floor(scholar_results)} BGN")

elif requirements_met_both and scholar_results >= social_scholarship:
    print(f"You get a scholarship for excellent results {floor(scholar_results)} BGN")

else:
    print(f"You get a Social scholarship {floor(social_scholarship)} BGN")
