# Part 1
# The following program will check if the triangle is equilateral or not


first= float(input('Enter the first number :'))
second=float(input('Enter the second number:'))
third= float(input('Enter the third number:'))
if (first == second== third):
    print('The triangle is equilateral ')
else:
    print('The triangle is not equal')


#Part 2
# The following program will check the relationship between two numbers
first= float(input('Enter the first number:'))
second= float(input('Enter second number:'))
print('The following are the relationships they satisfy: ')
if first < second:
    print(f'{first} < {second}')
if first > second:
    print(f'{first} > {second}')
if first <= second:
    print(f'{first} <= {second}')
if first >= second:
    print(f'{first} >= {second}')
if first == second:
    print(f'{first} == {second}')
else:
    print(f'{first} != {second}')


#Part 3
# The following program will calculate the average of the numbers entered by the user

number1 = int(input('Enter the number values ( between 1 and 10): '))
total_sum = 0
for count in range(number1):
    number = int(input(f'Enter a number {count +1} : '))
    total_sum = total_sum + number1

average = total_sum / number1
print(f'the total sum is {total_sum}')
print(f'The average is: {average}')


#Part 4
#this program prints a specific sequence of numbers 
for number in [1,22,333,4444,55555]:
    print (number)
print('\n')
