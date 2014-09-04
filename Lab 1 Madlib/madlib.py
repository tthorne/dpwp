'''
Student Name: Tara Thorne
Student Number: #0003809521
Assignment: Lab 1 Madlib
Date: Thursday, September 4, 2014
'''

# The Variables
name = raw_input('Enter a name: ')
color = raw_input('Enter a color: ')
animal = raw_input('Enter an animal: ')
fruit = raw_input('Pick a number between 1-5: ')
fruit_cost = raw_input('Enter the cost of the fruit: ')
many_fruit = raw_input('How many pieces of fruit do you want to buy? ')
dollar_amount = raw_input('Enter a dollar amount: ')

#Dictionary
fruit_name = dict() # Dictionary
fruit_name = {1:'Apples',2:'Bananas',3:'Cherries',4:'Grapes',5:'Oranges'}
fruit_type = int(fruit)
list_fruit = fruit_name[fruit_type]

#Function
def money(many_fruit,fruit_cost):
    total = many_fruit * fruit_cost
    return total

# Condition Statement
if money(int(many_fruit),int(fruit_cost)) < int(dollar_amount): # Mathematical
    current = int(dollar_amount)
    cost = int(fruit_cost)
    purchase = str(fruit)
    fruit_total = current - cost # Mathematical
    total_fruit = str(name) + ' can purchase ' + str(fruit_total) + ' ' + str(list_fruit)
else:
    total_fruit = str(name) + ' does not have enough cash to purchase ' + str(list_fruit)

    # Condition Statement
if money(int(many_fruit),int(fruit_cost)) > int(dollar_amount): # Mathematical
    current = int(dollar_amount)
    cost = int(fruit_cost)
    how_many = int(many_fruit)
    purchase = str(fruit)
    cash_needed = cost * how_many - cost # Mathematical
    cash = str(name) + ' needs $' + str(cash_needed) + ' more to purchase ' + str(list_fruit) + '.'
else: cash = ' Continue to check out.'

print name + ' went to the store riding a ' + color + ' ' + animal + ' to buy some ' + list_fruit + '. ' + 'The fruit costs $' + fruit_cost + ' and ' + name + ' brought $' + dollar_amount + ' and wants to buy ' + many_fruit + ' ' + list_fruit + '. ' + str(total_fruit) + '. ' + str(cash)