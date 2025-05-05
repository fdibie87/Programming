''' w5part1.py - String Manipulation Exercise
This script demonstrates various string operations in python 
'''
#1: Slitting a srting 
s = 'Python rules!'
word = s.split()
print(word)

#2: Lowercasing
print(s.lower())

#3: Finding a substring
print(s.find('rules'))

#4: Replacing a substring
print(s.replace('!','?'))

#5: Slicing a string
print(s[2:6])

#6: Reversing a string
print(s[::-1])

'''w5part2.py - String Comparison Program
This program compares two strings and let the user countinue ot quit 
'''
while True:
    first_string = input('Enter first string: ')
    second_string = input('Enter second string: ')

    if first_string < second_string:
        print(first_string,'\n',second_string)
    elif first_string > second_string:
        print(second_string,'\n', first_string)
    desicion = input('Enter y to continue or n to quit: ')

    if desicion == 'y':
        continue
    elif desicion == 'n':
        break