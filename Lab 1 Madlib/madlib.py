'''
Student Name: Tara Thorne
Student Number: #0003809521
Assignment: Lab 1 Madlib
Date: Thursday, September 4, 2014
'''

name = raw_input('Enter a name: ')
location = raw_input('Enter a location: ')
color = raw_input('Enter a color: ')
animal = raw_input('Enter an animal: ')
fruit = raw_input('Enter a fruit: ')
fruit_cost = raw_input('Enter the cost of the fruit: ')
many_fruit = raw_input('How many pieces of fruit do you want to buy? ')
dollar_amount = raw_input('Enter a dollar amount: ')

current = int(dollar_amount)
cost = int(fruit_cost)
total_fruit = current - cost

print name + ' went to ' + location + ' riding a ' + color + ' ' + animal + ' to buy some ' + fruit + '. ' + 'The fruit costs' + fruit_cost + ' and ' + name + ' brought $' + dollar_amount + ' so ' + str(total_fruit) + fruit + ' can be purchased.'