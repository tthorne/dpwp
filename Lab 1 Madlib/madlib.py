'''
Student Name: Tara Thorne
Student Number: #0003809521
Assignment: Lab 1 Madlib
Date: Thursday, September 4, 2014
'''

name = raw_input('Enter a name: ')
color = raw_input('Enter a color: ')
animal = raw_input('Enter an animal: ')
fruit = raw_input('Enter a fruit: ')
fruit_cost = raw_input('Enter the cost of the fruit: ')
many_fruit = raw_input('How many pieces of fruit do you want to buy? ')
dollar_amount = raw_input('Enter a dollar amount: ')

if int(many_fruit) * int(fruit_cost) < int(dollar_amount):
    current = int(dollar_amount)
    cost = int(fruit_cost)
    purchase = str(fruit)
    fruit_total = current - cost
    total_fruit = str(name) + ' can purchase ' + str(fruit_total) + ' ' + str(fruit) + "."
else:
    total_fruit = str(name) + ' does not have enough cash to purchase ' + str(fruit)

print name + ' went to the store riding a ' + color + ' ' + animal + ' to buy some ' + fruit + '. ' + 'The fruit costs $' + fruit_cost + ' and ' + name + ' brought $' + dollar_amount + ' and wants to buy ' + many_fruit + ' ' + fruit + '. ' + str(total_fruit)