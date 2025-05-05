#Part 1
# The following program will greet the user in different languages based on their country selection

print('Select the number of your Country:')
def country ():
    print(' 1.China\n 2.France\n 3.India\n 4.Spain\n 5.Quit program')
country()

name = input('Enter your name: ')
while True:
    choice = input('Enter choice (1, 2, 3, 4 or 5):')
    if choice == '1':
        print (f'Nǐ hǎo{name}')
    elif choice == '2':
        print(f'Bonjour {name}')
    elif choice == '3':
        print(f'Namaste{name}')
    elif choice == '4':
        print(f'Hola {name}')
    elif choice == '5':
        print(f'Thank you for playing! {name}')
        break
    else:
     print('Invalid Input')


#Part 2
# This program calculates the area of diffrent geometric shape 
import math
print('Calculate The Area of a Shape')
def shape ():
   print (" a) Rectangle\n b) Square\n c) Triangle\n d) Circle" )
shape()
choice = input('Enter the choice of shape whose area you want to find: ')

#Area calculation function
def area_of_rectangle(length,breadth):
    area1 = length*breadth
    return area1
def area_of_square(side):
    area = side*side
    return area
def area_of_triangle(base, height):
    area =0.5*base*height
    return area
def area_of_circle(radius):
    area = math.pi*radius**2
    return area

if choice == 'a':
    length = int(input("Enter rectangle's length: "))
    breadth = int(input("Enter rectangle's breadth: "))
    print(f'The area of rectangle is {area_of_rectangle(length,breadth)}.')
elif choice == 'b':
    side = int(input("Enter square's side: "))
    print(f'The area of square is {area_of_square(side)}.')
elif choice == 'c':
    base = int(input("Enter triangle's base: "))
    height = int(input("Enter triangle's height: "))
    print(f'The area of triangle is {area_of_triangle(base,height)}.')
elif choice == 'd':
    radius = int(input("Enter circle's radius: "))
    print(f'The area of circle is {area_of_circle(radius)}.')
else:
    print('Sorry! we cannot find this shape.')

    
#Part 3
# This program checks if the number is positive, negative or zero
def check_number(num):
    if num > 0 :
        print('positive') 
    elif num < 0:
        print('Negative')
    else:
        print ('zero')

