# - variable declaration
# -Data Type | Primitive | numbers
num1 = 42
num2 = 2.3
# -Data Type | Primitive | boolean
boolean = True
# -Data Type | Primitive | String
string = 'Hello World'
# -Data Type | Composite | List
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives']
# -Data Type | Composite | dictionary
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False}
# -Data Type | Composite | tuple
fruit = ('blueberry', 'strawberry', 'banana')
# - type check
print(type(fruit))
# - length check
print(pizza_toppings[1])
# List | change value
pizza_toppings.append('Mushrooms')
# Dictionary | access value
print(person['name'])
# Dictionary | change value & add value
person['name'] = 'George'
# Dictionary | change value & add value
person['eye_color'] = 'blue'
# List | access value
print(fruit[2])

# Conditional | if
if num1 > 45:
# log statement
    print("It's greater")
# Conditional | else
else:
# log statement
    print("It's lower")


# Conditional | if & length check
if len(string) < 5:
# log statement
    print("It's a short word!")
# Conditional | elif & length check
elif len(string) > 15:
# log statement
    print("It's a long word!")
# Conditional | else
else:
# log statement
    print("Just right!")


# for loop | start | variable declaration
for x in range(5):
    # log statement | access data
    print(x)
    # for loop | stop | increment

# for loop | start | variable declaration
for x in range(2,5):
    # log statement | access data
    print(x)
    # for loop | stop | increment

# for loop | start | variable declaration
for x in range(2,10,3):
    # log statement | access data
    print(x)
    # for loop | stop | increment

# variable declaration
x = 0
# while loop | start
while(x < 5):
    # log statement | access data
    print(x)
    # while loop | increment
    x += 1
    # while loop | stop

# function
pizza_toppings.pop()

#function | argument
pizza_toppings.pop(1)

#function | argument | log statement | access data
print(person)

#function | argument 
person.pop('eye_color')

#function | argument | log statement | access data
print(person)


# for loop | variable declaration | data type | composit | list
for topping in pizza_toppings:
    # conditional | if
    if topping == 'Pepperoni':
        # for loop | continue
        continue
    # log statement
    print('After 1st if statement')
    # conditional | if
    if topping == 'Olives':
        # for loop | break
        break


# function
def print_hello_ten_times():
    # for loop | variable declaration
    for num in range(10):
        # log statement
        print('Hello')


# function argument
print_hello_ten_times()

# function parameter
def print_hello_x_times(x):
    # for loop | start | variable declaration
    for num in range(x):
        # log statement
        print('Hello')


# function argument
print_hello_x_times(4)


# function parameter
def print_hello_x_or_ten_times(x = 10):
    # for loop | start | variable declaration
    for num in range(x):
        # log statement
        print('Hello')


# function argument
print_hello_x_or_ten_times()
# function argument
print_hello_x_or_ten_times(4)





"""

Bonus section

"""


# - NameError: name <variable name> is not defined
# print(num3)

# num3 = 72

# - TypeError: 'tuple' object does not support item assignment
# fruit[0] = 'cranberry'

# - KeyError: 'favorite_team'
# print(person['favorite_team'])

# - IndexError: list index out of range
# print(pizza_toppings[7])

# - IndentationError: unexpected indent
#   print(boolean)

# - AttributeError: 'tuple' object has no attribute 'append'
# fruit.append('raspberry')

# - AttributeError: 'tuple' object has no attribute 'pop'
# fruit.pop(1)