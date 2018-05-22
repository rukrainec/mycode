#!/usr/bin/env python3
# custom script to play with functionality of if/elif operators
# goal: user inputs any number, script determines how that number relates to a letter grade
message = 'Congratulations, your grade for this course is '
print('What did you get on the final?')
grade = float(input())
if grade > 100:
	message = 'That isn\'t possible you cheater' # to cover invalid grades above 100%
elif grade >= 90:
    message = message + 'A! Well done!'
elif grade >= 80:
    message = message + 'B'
elif grade >= 70:
    message = message + 'C, mediocrity at its finest'
elif grade >= 60:
	message = message + 'D. Your parents must be proud.'
elif grade >= 0:
	message = message + 'F.'
elif grade < 0:
	message = 'How did you get a negative score? This isn\'t Jeopardy.' #to cover invalid grades blow 0%
print(message)
