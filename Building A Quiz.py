 #Building a Python Quiz Using Conditionals

# Setting up Quiz Framework
name = input('What is your name:')
txt = f'Hello {name} welcome'
print (txt)
print('You are going to be taking a short 5 question quiz about Music!!')
print('Your will be answering the questions in a format of a,b,c or d.\n')
print ('Input only the letter')

#Initialize score Variable and Creating questions
print('Question 1')
print('What instrument is the most common played in elementary school?' )
score = 0
answer1 = input(' a)Drums\n b)Piano\n c)Recorder\n d)Guitar\nEnter your answer:')
if answer1 == 'c':
    print('Correct!')
    score+= 1
else:
    print('Incorrect. The correct answer is c)Recorder')

print('Question 2')
print('What artist sang this song "The Colour Violet"?')
answer2 = input(' a)Tory Lanez\n b)Drake\n c)Stevie Wonder\n d)Elvis Presley\nEnter your answer:')
if answer2 == 'a':
    print('Correct!')
    score +=1
else:
    print ('Incorrect. The correct answer is a)Tory Lanez')

print('Question 3')
print('What is a commonly used instrument? ')

answer3 = input(' a)Guitar\n b)Piano\n c)Saxophone\n d)Trumpet\nEnter your answer: ')

if answer3 =='b':
    print('Correct!')
    score += 1
else:
    print('Incorrect. the correct answer is b)Piano')

print('Question 4')
print("Who is Canada's no 1 rap artist? ")
answer4 = input(' a)Tory Lanez\n b)Kendrick Larmer\n c)The Weeknd\n d)Drake\nEnter your answer: ')
if answer4 == 'd':
    print('Correct!')
    score += 1
else:
    print('Incorrect. The correct answer is d)Drake')

print('Question 5')
print('How many letters in the Musical Alphabet?')
answer5 = input(' a) 5\n b) 7\n c) 10\n d) 12\nEnter your answer:')
if answer5 == 'b':
    print('Correct!')
    score += 1
else:
    print('Incorrect. The correct answer is b)7')
# Final Score and Feedback
print(f'\n Your final score is {score}/5')
if score == 5:
    print('Excellent! You got all answers correct!')
elif score >= 3:
    print('Good job! You scored above average.')
else:
    print('You might want to study more.')

print(f'Thank you {name} for taking the quiz! ')


