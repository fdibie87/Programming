#Part 1: Temperature Analysis 
# This program collects daily temperatures and computes mean, min, max and standard deviation of temperature

import statistics
def analyze_temperature():

 '''
The purpose of the function is to collect daily temperatures,
compute mean, minimum, maximum and standard deviation of temperature
'''
number_of_days = int(input('Enter number of days the event days:'))
temperatures = []
for i in range(1,number_of_days +1):
    temps = float(input(f'Enter the maximum temperature recorded on that day {str(i)}:'))
    temperatures.append(temps)
mean = statistics.mean(temperatures)
minimum = min(temperatures)
maximum = max(temperatures)
standard_deviation = statistics.stdev(temperatures)
print(f'Temperature values:{temperatures}\n')
print('Temperature Statistics')
print(f'Mean: {mean:.2f}')
print(f'Min: {minimum:.2f}')
print(f'Max: {maximum:.2f}')
print(f'Standard Deviation: {standard_deviation:.2f}')

#Part 2: Expense Tracking
#Function to track and display daily expenses
def track_expenses():
    '''Purpose to track expenses across multiple categories each day of event '''
    event_day = int(input('Enter the number of event day:'))
    expenses = []
    for i in range(1,event_day+1):
        print(f'Day {i}')
        vre =  input(f'Enter expenses for venue, equipment and refreshment for Day {i} seperated by spaces:' )
        venue_expense, refreshment_expense, equipment_expense = map(float,vre.split())
        nested_list = [i, venue_expense, refreshment_expense, equipment_expense ]
        expenses.append(nested_list)

    print('Daily Expenses:')
    for  day, venue_expense, refreshment_expense, equipment_expense in expenses:
        total_expense = venue_expense + refreshment_expense + equipment_expense
        print(f'Day {day}: Total = {total_expense:.2f}')

    return expenses

track_expenses()

#part 3
def manage_score():
 '''Purpose to record athelete names, score, and calculate averages '''
 num_of_athletics = int(input('Enter number of athletes participating: '))
 scores = []
 for i in range(1,num_of_athletics+1):
    name = input('Enter athlete name: ')
    scores_input= input(f'Enter score for {name} in three events seperated by spaces:')
    Score1, Score2, Score3 = map(float,scores_input.split())
    nested_list = [name, Score1, Score2, Score3]
    scores.append(nested_list)
print('Average Scores:')
for athlete in score:
        name,Score1,Score2,Score3 = athlete
        total = Score1 + Score2 + Score3
        average = sum(score) /len(3)
        print(f'{name}:{average:.2f}')
threshold = float(input('Enter a score threshold: '))
print('High Performers:')
if average >= threshold:
        print(f'{name}:{average:.2f}')
else:
      quit()
manage_score()

def main():
    print('Welcome to the Sport Event Data Analysis Workshop!')
    analyze_temperature()
    track_expenses()
    manage_score()
if name ==' main':
    main()