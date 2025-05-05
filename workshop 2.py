#calculate the momentum of superhero

# Part 1
'''Write a program that calculates the momentum of a superhero's flying kick. Imagine a superhero is 
flying towards a target, and you need to calculate the momentum of their kick. The momentum is 
calculated using the formula momentum = mass * velocity. Prompt the user to input the superhero's 
mass (in kilograms) and velocity (in meters per second). Use conditional statements to provide different 
responses based on the momentum calculated: 
- If the momentum is greater than 1000, display a message saying "Super kick! The target is going 
flying!" 
- If the momentum is between 500 and 1000, display "Decent hit! The target is knocked back." 
- If the momentum is less than 500, display "Hmm, needs more power!"
'''

mass = int(input('Enter the superhero mass number:',))
velocity = int(input('Enter the superhero velocity:'))
momentum = mass * velocity

print ('The momentum is:',f"{momentum} kgm/s")

if momentum > 1000:
    print('Super kick! The target is goin flying!')
elif momentum > 500 or momentum < 1000:
    print('Decent hit! The target is knocked back')
else :
    print('Hmm, needs more power!')

# Part 2
'''You are designing a smart thermostat for a smart home system. Write a program that adjusts the 
temperature of a house based on the outside weather. The program should: 
1. Take the current outside temperature as input. 
2. Use conditional statements to set the inside temperature: 
o If the outside temperature is below 15°C, set the inside temperature to 22°C. 
o If the outside temperature is above 25°C, set the inside temperature to 20°C. 
o If the outside temperature is between 15°C and 25°C, set the inside temperature to 21°C. 
o In any other case, set the inside temperature to 18°C. 
3. In each case, display the chosen inside temperature and a friendly message, such as "Warming 
up your morning!" or "Cooling down the afternoon heat!" 
'''
outside_temp = int(input('what is the current temperature:'))

if outside_temp < 15:
    inside_temp= 22
    print(inside_temp , 'degrees','warming up your morning')

elif outside_temp > 25:
    inside_temp1 = 20
    print(inside_temp1 , 'degrees','cooling down the afternoon heat')
elif outside_temp >=15 <=25:
    inside_temp2 = 21
    print(inside_temp2, 'degrees','cooling down the afternoon heat')
else:
    print('degree Lets cool down your morning')

#Part 3
'''
Write a program for an online store that calculates the total price of a purchase after applying discounts. 
The program should: 
1. Take the total purchase amount as input. 
2. Use conditional statements to apply discounts
'''
total_purchase = float(input('What is the total purchase amount:'))

if total_purchase > 100:
    total_after_discount1 = total_purchase * (1-0.10)
    print('Total purchase after discount =', round(total_after_discount1,2))
    print('The finial price after discount is',round(total_after_discount1),1)
elif total_purchase > 200:
    total_after_discount2 = total_purchase * (1-0.20)
    print('Total purchase after discount = ', round(total_after_discount2,2))
    print('The finial price after discount is',round(total_after_discount2,1))
else:
    print('No discount applied. Total purchase =', round(total_purchase, 2))


#part 4
'''Create a grade classification program that categorizes student grades based on a numeric input. The 
program should: 
1. Take the student's numeric grade (0 to 100) as input. 
2. Use conditional statements to classify the grade: 
o If the grade is 90 or above, classify it as "A". 
o If the grade is between 80 and 89, classify it as "B". 
o If the grade is between 70 and 79, classify it as "C". 
o If the grade is between 60 and 69, classify it as "D". 
o If the grade is below 60, classify it as "F". 
3. Display the letter grade classification along with a message like "Excellent work!" or "Needs Improvement."
'''

student_grade = int(input('Enter the student grade:'))
if student_grade > 90:
    print('The student grade is A','Excellent Work')
elif student_grade >= 80 <= 89:
    print('The student grade is B','Excellent work')
elif student_grade >= 70 <= 79:
    print('The student grade is C','Needs Improvement')
elif student_grade >= 60 <= 69:
    print('The student grade is D','Needs Improvement')
else:
    print('The student grade is F','Needs Improvement')

