num1 = 42 #variable declaration, Numbers, initialize
num2 = 2.3#variable declaration, Numbers, initialize
boolean = True#type check, Boolean
string = 'Hello World'#variable declaration , Strings
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives']#variable declaration, Strings, List
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False}#variable declaration, type check, Strings, Dictionary
fruit = ('blueberry', 'strawberry', 'banana')#variable declaration, Strings, Tuples
print(type(fruit))#log statement, type check, access value
print(pizza_toppings[1])#log statement , access value
pizza_toppings.append('Mushrooms')#Strings, add value
print(person['name'])#log statement, Strings, access value
person['name'] = 'George'#variable declaration, Strings,change value
person['eye_color'] = 'blue'#variable declaration, Strings, change value
print(fruit[2])#log statement, access value

if num1 > 45:
    print("It's greater")
else:
    print("It's lower")
#log statement, Strings, conditional, 
if len(string) < 5: 
    print("It's a short word!")
elif len(string) > 15:
    print("It's a long word!")
else:
    print("Just right!")
#log statement, length check, Strings, conditional, 
for x in range(5):
    print(x)
for x in range(2,5):
    print(x)
for x in range(2,10,3):
    print(x)
x = 0 
#variable declaration, Numbers, change value, for loop
while(x < 5):
    print(x)
    x += 1
#log statement, Numbers, while loop
pizza_toppings.pop()#delete value
pizza_toppings.pop(1)#delete value

print(person)#log statement
person.pop('eye_color')#Strings, delete value
print(person)#log statement

for topping in pizza_toppings:
    if topping == 'Pepperoni':
        continue
    print('After 1st if statement')
    if topping == 'Olives':
        break
#log statement, Strings, conditional, for loop
def print_hello_ten_times():
    for num in range(10):
        print('Hello')
#log statement, Strings, function
print_hello_ten_times()
#log statement
def print_hello_x_times(x):
    for num in range(x):
        print('Hello')
#log statement, Strings, function
print_hello_x_times(4)
#log statement
def print_hello_x_or_ten_times(x = 10):
    for num in range(x):
        print('Hello')
#log statement, Strings, function, for loop
print_hello_x_or_ten_times()#log statement
print_hello_x_or_ten_times(4)#log statement