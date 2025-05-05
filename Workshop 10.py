#Part 1: inventory analysis 
inventory = {'apples': 50,
             'banana': 120,
             'orange': 80,
             'grapes': 45,
             'pears': 60}

total = sum(inventory.values ())
average = total / 5
print(f'The total sum is {total}')
print(f'the average is {average}')

# looking for the length in the total keys each word


total_length_sum = sum(key.values) 
for key in inventory.keys():
 average1 = total_length_sum / len(inventory)

print(f'The sum of product name is {total_length_sum}')
print(f'The average is {average1}')

#Part 2: Order Processing System
# This program allows the user to input orders and calculates the total and average quantity of items ordered.
sample_order = {'apples':[5,10,4],
                'bananas':[3,7,8,2],
                'orange':[6,5],
                'grapes':[2,3,3,4]}

name = input('Enter you name:')
print(f'Hey {name}')
num_of_orders = int(input('Enter how many items do you want to order?:'))

def input_order(orders):
    for i in range(num_of_orders):
        item =  input('Enter name of item:')
        quantities = int(input('Enter quantity of item:'))

        if item in orders:
            orders[item].append(quantities)
        else:
            orders[item] = [quantities]

    return orders

def make_orders_dict(orders,num_of_orders):
   return input_order(orders)

def calculate_order_stats(order_dict):
    total_item = 0
    total_orders = 0
    for item, quantities in order_dict.items():
        total_item += sum(quantities)
        total_orders += len(quantities)
    average = round(total_item/ total_orders, 2)


    print(f'Total ordered items {total_item}')
    print(f'Average quantity per item {average} ')


sample_order = make_orders_dict(sample_order, num_of_orders)
calculate_order_stats(order_dict = sample_order)
#PART 3: Country and Capital Management System
countries_and_capitals = {'Canada':'Ottawa',
                            'France':'Paris',
                            'Japan':'Tokyo',
                            'India':'New Delhi',
                            'Brazil':'Brasilia'}
decision = input('Would you like to (R)etrieve a capital, (A)dd a country, or (Q)uit?:  ').upper()
def get_capital(country):
    if country in countries_and_capitals:
        return f'the capital of {country} is : {countries_and_capitals[country]}'
    else:
            return
def add_country(country,capital):
    if country in countries_and_capitals:
        return countries_and_capitals[country]+capital
    else:
        countries_and_capitals[country] = capital

def letters(decision):
 while True:

    if decision == 'R':
        country = input('Enter the country name: ')
        print(get_capital(country))
    elif decision == 'A':
        country1 = input('Enter the country name: ').strip()
        capital1 = input('Enter the capital is: ').strip()
        print(f'{country1} is a add to the list anf the capital{capital1} ')
        countries_and_capitals[country1] = capital1

    elif decision == 'A':
        country2 = input('Enter the country name: ').strip()
        capital2 = input('Enter the capital is: ').strip()
        if country2 in countries_and_capitals:
            print(f'{country2} is a add to the list and the capital {capital2} ')
            print(add_country(country2,capital2))
        else:
            return
    elif decision == 'Q':
        print('Exiting the program')
    return
letters(decision)








