# a program that uses the AnonymousSurvey class in survey.py
from survey import AnonymousSurvey

my_survey = AnonymousSurvey("\nEnter your native tongue or enter 'q' to quit\n")

my_survey.show_question()

while True:
    response = input('* Response: ')

    if response == 'q':
        break

    my_survey.store_response(response)

print('----------------------')

my_survey.show_results()
