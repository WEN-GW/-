# def print_num(x):
#     print(f"传入的参数为: {x}")
#     return 
# print(10) # <class 'function'>


# def print_num(x,y):
#     print(f"传入的参数为: {x}")
#     print(f"传入的参数为: {y}")
#     return 
# print_num(y=10,x=9)
# print_num(y=130,x=30)# <class 'function'>



# def add_numbers(x,y):
#     return x+y
# result = add_numbers(10,20)
# print(result)


# def get_name_and_age():
#     name = "Alice"
#     age = 25
#     return name, age
# name, age = get_name_and_age()
# print(f"Name: {name}, Age: {age}") # Name: Alice, Age: 25


# def test_function():
#     local_variable = 10
#     print(local_variable)
# test_function()



# a = 5
# print(id(a))
# a = 10
# print(id(a)
# 
# 
# 
# la = [1,2,3,4,5,6,7,8,9,10]
# print(id(la))
# la[1]=100
# print(id(la))
# print(la)



# def changeint(a)
#     a = 10
# b = 2
# changeint(b)
# print(b)







# def multiply_num(x,y):
#     return x*y
# print(multiply_num(10,20))


# multipiy = lambda x,y: x*y
# print(multipiy(10,20))



# def test_lambda(x,y,func):
#     print(func(x,y))
# test_lambda(10,20,lambda x,y: x+y)



# L = list(filter(lambda x: x % 2 == 1, range(1, 11)))
# print(L)


# multiply_func=lambda x,y:x*y
# print(multiply_func(10,5))




# def counter():
#     count = 0
#     def change_count():
#         nonlocal count
#         count += 1
#         return count
#     return change_count
# # c = counter()
# # print(c())
# # print(c())
# # print(c())

# def test(func):
#     print(func())
# test(counter())



# def say_hello(func):
#     def print_hello():
#         print("Hello")
#         func()
#     return print_hello

# @say_hello
# def say_world():
#     print("World")

# say_world()



# def counter():
#     count = 100
#     def change_count():
#         nonlocal count
#         if count<0:
#             return 0
#         current=count
#         count -= 1
#         return current
#     return change_count

# c=counter()
# # print(c())
# # print(c())
# for x in range(1,150):
#     print(c())





# def fact(num):
#     print(num)
#     if num==1:
#         return 1
#     else:
#         return num*fact(num-1)
# print(fact(5))





# def multipiy_func(x,n):
#     if n==0:
#         return 1
#     else:
#         return x*multipiy_func(x,n-1)
# print(multipiy_func(2,5))



# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# result = 0
# for num in numbers:
#     if num % 2 == 0:
#         squared = num *num
#         result += squared
# print(f"结果是:{result}")


# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# def is_even(num):
#     return num % 2 == 0
# def square(number):
#     return number * number
# def sum_of_even_squares_function(numbers):
#     even_numbers = []
#     for num in numbers:
#         if is_even(num):
#             even_numbers.append(num)

#     squared_numbers = []
#     for num in even_numbers:
#         squared_numbers.append(square(num))
#     total = 0
#     for num in squared_numbers:
#         total += num
#     return total
# result = sum_of_even_squares_function(numbers)
# print(result)







# def my_for_each(func,items):
#     for item in items:
#         func(item)
# def print_number(x):
#     print(f"数字:{x}")
# def print_square(x):
#     print(f"数字的平方:{x*x}")
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# my_for_each(print_number,numbers)




# This program says hello and asks for my name.

# print('Hello, world!')
# print('What is your name?')  # Ask for their name.
# my_name = input('>')
# print('It is good to meet you, ' + my_name)
# print('The length of your name is:')
# print(len(my_name))
# print('What is your age?')  # Ask for their age.
# my_age = input('>')
# print('You will be ' + str(int(my_age) + 1) + ' in a year.')



# print('The length of your name is:')
# print(len(my_name))


# type(42)



# print(type(42))
# print(type(42.2))
# print(type("forty two"))
# name = "Zophie"
# print(type(name))
# type(len(name))
# print(type(len(name)))




# print(round(3.14))
# print(round(3.4))
# print(round(7.7))
# print(round(-3.3))
# print(round(-7.3))
# print(round(3.14,1))
# print(round(7.7777,3))
# print(abs(-42))
# print(abs(42))
# print(abs(-3.14))
# print(abs(0))

# bacon = 20
# a = bacon + 1
# print(a)


# spam = True
# print(spam)

# 42 == 42
# 42 == 99
# 2 != 3
# 2 != 2



# print(4 < 5) and (5 < 6)
# print(4 < 5) and (9 < 6)
# print(1 == 2) or (2 == 2)




# spam = 4
# print(2 + 2 ==spam and not 2 + 2 == (spam + 1) and 2 * 2 == 2 + 2)


# username = input("请输入用户名：")
# password = input("请输入密码：")
# username = "Mary"
# password = "swordfish"
# if username == "Mary":
#     print("Hello, Mary")
#     if password == "swordfish":
#         print("Access granted")
#     else:
#         print("Wrong password")



# name = "Alice"
# if name == "Alice":
#     print("Hi,Alice")
# else:    
#     print("Hello,Stranger")


# name = str(input("请输入你的名字："))
# age = int(input("请输入你的年龄："))
# name = "Alire"
# age = 10
# if name == "Alice":
#     print("Hi,Alice")
# elif age < 12:
#     print("You are not Alice, kiddo.")
# else:
#     print("名字错误")


# name = str(input("请输入你的名字："))
# age = int(input("请输入你的年龄："))
# name = "Alire"
# age = 10
# if name == "Alice":
#     print("Hi,Alice")
# elif age < 12:
#     print("You are not Alice, kiddo.")
# else:
#     print("名字错误")




# name = "Alic"
# age = 11
# if name == "Alice":
#     print("Hi,Alice")
# elif age < 12:
#     print("You are not Alice,kiddo.")
# elif age > 2000:
#     print("Unlike you,Alice is not an undead,immortal vampire.")
# elif age >100:
#     print("You are not Alice,grannie.")
        


# name = "Alic"
# age = 300
# if name == "Alice":
#     print("Hi,Alice")
# elif age < 12:
#     print("You are not Alice,kiddo.")
# elif age > 1000:
#     print("Unlike you,Alice is not an undead,immortal vampire.")
# elif age > 5000:
#     print("You are not Alice,grannie.")
# else:
#     print("You are neither Alice nor a little kid.")



# today_is_opposite_day = True
# # Set say_it_is_opposite_day based on today_is_opposite_day:
# if today_is_opposite_day == True:
#     say_it_is_opposite_day = True
# else:
#     say_it_is_opposite_day = False

# # If it is opposite day, toggle say_it_is_opposite_day:
# if today_is_opposite_day == True:
#     say_it_is_opposite_day = not say_it_is_opposite_day

# # Say what day it is:
# if say_it_is_opposite_day == True:
#     print("Today is opposite Day.")
# else:
#     print("Today is not Opposite Day.")

# true False
# and or not
# and 两个的要真才真  or 一个要真就真   not 取反
# == != < > <= >=
#False False true False False true
#  == 比较  = 赋值



# spam = 0
# if spam < 5:
#     print("Hello")
#     spam = spam + 1


# spam = 0
# if spam < 5:
#     print("Hello")
#     spam = spam + 1


# spam = 0
# while spam < 5:
#     print("Hello")
#     spam = spam + 1


# spam = 6
# if spam < 5:
#     print("Hello")
#     spam = spam + 1


# spam = 6
# while spam < 5:
#     print("Hello")
#     spam = spam + 1




# spam = 4
# while spam < 5:
#     print("Hello")
#     spam = spam + 1




# name = ""
# while name != "your name":
#     print("Please type your name.")
#     name = input(">")
# print("Thank you!")


# while True:
#     print("Please type your name.")
#     name = input(">")
#     if name == "your name":
#         break
# print("Thank you!")

# while True:
#     print("Who are you?")
#     name = input(">")
#     if name != "Joe":
#         continue
#     print("Hello, Joe. What is the password? (It is a fish.)")
#     password = input(">")
#     if password == "swordfish":
#         break
# print("Access granted.")


# truthy    falsey    bool


# name = ""
# while not name:
#     print("Enter your name.")
#     name = input(">")
# print("How many guests will you have")
# num_of_guests = int(input(">")
# if num_of_guests:
#     print("Be sure to have enough room for all your guests.")
# print("Done")


# print(bool(0))
# print(bool(42))
# print(bool("spam"))
# print(bool([]))



# print("Hello!")
# for i in range(5):
#     print('On this iteration, i is set to ' + str(i))
# print("Goodbye!")



# total = 0
# for num in range(101):
#     total = total + num
# print(total)


# print("Hello!")
# i= 0
# while i < 5:
#     print('On this iteration, i is set to ' + str(i))
#     i = i + 1
# print("Goodbye!")



# for i in range(1, 6):
#     print(i)



# for i in range(0, 10, 2):
#     print(i)


# for i in range(5, -1, -1):
#     print(i)




# import random
# for i in range(5):
#     print(random.randint(1, 10))






# import sys

# while True:
#     print('Type exit to exit.')
#     response = input('>')
#     if response == 'exit':
#         sys.exit()
#     print('You typed ' + response + '.')





# print("I am thinking of a number between 1 and 20.")
# Take a guess.




# This is a guess the number game.
# import random
# secret_number = random.randint(1, 20)
# print('I am thinking of a number between 1 and 20.')

# # Ask the player to guess 6 times.
# for guesses_taken in range(1, 7):
#     print('Take a guess.')
#     guess = int(input('>'))

#     if guess < secret_number:
#         print('Your guess is too low.')
#     elif guess > secret_number:
#         print('Your guess is too high.')
#     else:
#         break  # This condition is the correct guess!

# if guess == secret_number:
#     print('Good job! You got it in ' + str(guesses_taken) + ' guesses!')
# else:
#     print('Nope. The number was ' + str(secret_number))



# import random, sys

# print('ROCK, PAPER, SCISSORS')

# # These variables keep track of the number of wins, losses, and ties.
# wins = 0
# losses = 0
# ties = 0

# while True:  # The main game loop
#     print('%s Wins, %s Losses, %s Ties' % (wins, losses, ties))
#     while True:  # The player input loop
#         print('Enter your move: (r)ock (p)aper (s)cissors or (q)uit')
#         player_move = input('>')
#         if player_move == 'q':
#             sys.exit()  # Quit the program.
#         if player_move == 'r' or player_move == 'p' or player_move == 's':
#             break  # Break out of the player input loop.
#         print('Type one of r, p, s, or q.')

#     # Display what the player chose:
#     if player_move == 'r':
#         print('ROCK versus...')
#     elif player_move == 'p':
#         print('PAPER versus...')
#     elif player_move == 's':
#         print('SCISSORS versus...')

#     # Display what the computer chose:
#     move_number = random.randint(1, 3)
#     if move_number == 1:
#         computer_move = 'r'
#         print('ROCK')
#     elif move_number == 2:
#         computer_move = 'p'
#         print('PAPER')
#     elif move_number == 3:
#         computer_move = 's'
#         print('SCISSORS')

#     # Display and record the win/loss/tie:
#     if player_move == computer_move:
#         print('It is a tie!')
#         ties = ties + 1
#     elif player_move == 'r' and computer_move == 's':
#         print('You win!')
#         wins = wins + 1
#     elif player_move == 'p' and computer_move == 'r':
#         print('You win!')
#         wins = wins + 1
#     elif player_move == 's' and computer_move == 'p':
#         print('You win!')
#         wins = wins + 1
#     elif player_move == 'r' and computer_move == 'p':
#         print('You lose!')
#         losses = losses + 1
#     elif player_move == 'p' and computer_move == 's':
#         print('You lose!')
#         losses = losses + 1
#     elif player_move == 's' and computer_move == 'r':
#         print('You lose!')
#         losses = losses + 1






# def hello():
#     # Prints three greetings
#     print('Good morning!')
#     print('Good afternoon!')
#     print('Good evening!')

# hello()
# hello()
# print('ONE MORE TIME!')
# hello()





# def say_hello_to(name):
#     # Prints three greetings to the name provided
#     print('Good morning, ' + name)
#     print('Good afternoon, ' + name)
#     print('Good evening, ' + name)

#   say_hello_to('Alice')
# say_hello_to('Bob')
# ood afternoon, Alice
# Good evening, Alice
# Good morning, Bob
# Good afternoon, Bob
# Good evening, Bob



# def say_hello_to(name):
#     # Prints three greetings to the name provided
#     print('Good morning, ' + name)
#     print('Good afternoon, ' + name)
#     print('Good evening, ' + name)
# say_hello_to('Al')




# import random

# from 循环 import i

# def get_answer(answer_number):
#     # Returns a fortune answer based on what int answer_number is, 1 to 9
#     if answer_number == 1:
#         return 'It is certain'
#     elif answer_number == 2:
#         return 'It is decidedly so'
#     elif answer_number == 3:
#         return 'Yes'
#     elif answer_number == 4:
#         return 'Reply hazy try again'
#     elif answer_number == 5:
#         return 'Ask again later'
#     elif answer_number == 6:
#         return 'Concentrate and ask again'
#     elif answer_number == 7:
#         return 'My reply is no'
#     elif answer_number == 8:
#         return 'Outlook not so good'
#     elif answer_number == 9:
#         return 'Very doubtful'

# print('Ask a yes or no question:')
# input('>')
# r = random.randint(1, 9)
# fortune = get_answer(r)
# print(fortune)




# raise Exception('This is an error message')
# Traceback (most recent call last):
#   File "<pyshe11#191>", line 1, in <module>
#     raise Exception('This is an error message')
# Exception: This is an error message



# def box_print(symbol, width, height):
#     if len(symbol) != 1:
#         raise Exception('Symbol must be a single character string.')
#     if width <= 2:
#         raise Exception('Width must be greater than 2.')
#     if height <= 2:
#         raise Exception('Height must be greater than 2.')
#     print(symbol * width)
#     for i in range(height - 2):
#         print(symbol + ' ' * (width - 2) + symbol)
#     print(symbol * width)

# try:
#     box_print('*', 4, 4)
#     box_print('0', 20, 5)
#     box_print('x', 1, 3)
#     box_print('ZZ', 3, 3)
# except Exception as err:
#     print('An error occurred: ' + str(err))
# try:
#     box_print('ZZ', 3, 3)
# except Exception as err:
#     print('An error occurred: ' + str(err))





# ages = [26, 57, 92, 54, 22, 15, 17, 80, 47, 73]
# ages.sort()
# print(ages)
# assert ages[0] <= ages[-1]  # Assert that the first age is <= the last age.



# ages = [26, 57, 92, 54, 22, 15, 17, 80, 47, 73]
# ages.reverse()
# print(ages)
# assert ages[0] <= ages[-1]  # Assert that the first age is <= the last age.
# Traceback (most recent call last):
#   File "<python-input-0>", line 1, in <module>
# AssertionError






# import logging
# logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s -  %(levelname)s -  %(message)s')



# import logging
# logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s -  %(levelname)s -  %(message)s')
# logging.debug('Start of program')
# def factorial(n):
#     logging.debug('Start of factorial(' +str(n) + ')')
#     total = 1
#     for i in range(n + 1):
#         total *= i
#         logging.debug('i is ' + str(i) + ', total is ' + str(total))
#     logging.debug('End of factorial(' + str(n) + ')')
#     return total

# print(factorial(5))
# logging.debug('End of program')



# import logging
# logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s -  %(levelname)s -  %(message)s')
# logging.debug('Start of program')
# def factorial(n):
#     logging.debug('Start of factorial(' +str(n) + ')')
#     total = 1
#     for i in range(1, n + 1):
#         total *= i
#         logging.debug('i is ' + str(i) + ', total is ' + str(total))
#     logging.debug('End of factorial(' + str(n) + ')')
#     return total

# print(factorial(5))
# logging.debug('End of program')



# import logging
# logging.basicConfig(filename='myProgramLog.txt', level=logging.DEBUG,
# format=' %(asctime)s -  %(levelname)s -  %(message)s')



# import logging




# import random
# heads = 0
# for i in range(1, 1001):
#     if random.randint(0, 1) == 1:
#         heads = heads + 1
#     if i == 500:
#         print('Halfway done!')
# print('Heads came up ' + str(heads) + ' times')






# import random
# guess = ''
# while guess not in ('heads', 'tails'):
#     print('Guess the coin toss! Enter heads or tails:')
#     guess = input()
# toss = random.randint(0, 1)  # 0 is tails, 1 is heads
# if toss == guess:
#     print('You got it!')
# else:
#     print('Nope! Guess again!')
#     guess = input()
#     if toss == guess:
#         print('You got it!')
#     else:
#         print('Nope. You are really bad at this game.')



# print(['1, 2, 3'])
# print(['cat', 'bat', 'rat', 'elephant'])
# print(['hello', 3.1415, True, None, 42])
# spam = ['cat, bat, rat, elephant']
# print(spam)


# spam = ['cat, bat, rat, elephant']
# print(spam[0])

# spam = ('cat', 'bat', 'rat', 'elephant')
# print(spam[3])





# spam = ['cat', 'bat', 'rat', 'elephant']
# print(spam[10000])
# Traceback (most recent call last):
#   File "<python-input-0>", line 1, in <module>
#     spam[10000]
# IndexError: list index out of range



# spam = ['cat', 'bat', 'rat', 'elephant']
# print(spam[1:3])
# print(spam[-1])
# print(spam[0:4:2])
# print(spam[:2])
# print('The ' + spam[-1] + ' is afraid of the' + spam[-3] + '.')



# spam = ['cat', 'bat', 'rat', 'elephant']
# print(spam[0:4])
# print(spam[1:3])
# print(spam[0:-1])



# spam = ['cat', 'bat', 'rat', 'elephant']
# print(spam[:2])
# print(spam[1:])
# print(spam[:])




# spam = ['cat', 'dog', 'moose']
# print(len(spam))




# spam = ['cat', 'bat', 'rat', 'elephant']
# spam[1] = 'aardvark'
# print(spam)
# spam[2] = spam[1]
# print(spam)
# spam[-1] ='12345'
# print(spam)



# a = [1, 2, 3] + ['A','B', 'C']
# print(a)
# b = [1, 2, 3] * 3
# print(b)
# spam = [1, 2, 3]
# spam = spam + ['A', 'B', 'C']
# print(spam)



# spam = ['cat', 'bat', 'rat', 'elephant']
# del spam[2]
# print(spam)
# del spam[2]
# print(spam)



# cat_name_1 = 'Zophie'
# cat_name_2 = 'Pooka'
# cat_name_3 = 'Simon'
# cat_name_4 = 'Lady Macbeth'
# print(cat_name_1 + ' and ' + cat_name_2 + ' and ' + cat_name_3 + ' and ' + cat_name_4)
# print(cat_name_1, cat_name_2, cat_name_3, cat_name_4)



# print('Enter the name of cat 1:')
# cat_name_1 = input()
# print('Enter the name of cat 2:')
# cat_name_2 = input()
# print('Enter the name of cat 3:')
# cat_name_3 = input()
# print('Enter the name of cat 4:')
# cat_name_4 = input()
# print('The cat names are:')
# print(cat_name_1 + ' and ' + cat_name_2 + ' and ' + cat_name_3 + ' and ' + cat_name_4)


# print('Enter the name of cat 1:')
# cat_name_1 = input()
# print('Enter the name of cat 2:')
# cat_name_2 = input()
# print('Enter the name of cat 3:')
# cat_name_3 = input()
# print('Enter the name of cat 4:')
# cat_name_4 = input()
# print('The cat names are:')
# print(cat_name_1 + cat_name_2 + cat_name_3 + cat_name_4)


# cat_names = []
# while True:
#     print('Enter the name of cat ' + str(len(cat_names) + 1) + ' (Or enter nothing to stop.):')
#     name = input()
#     if name == '':
#         break
#     cat_names = cat_names + [name]
# print('The cat names are:')
# for name in cat_names:
#     print('  ' + name)



# for i in range(4):
#     print(i)


# for i in [0, 1, 2, 3]:
#     print(i)




# supplies = ['pens', 'staplers', 'flamethrowers', 'binders']
# for i in range(len(supplies)):
#     print('Index ' + str(i) + ' in supplies is: ' + supplies[i])





import pathlib
from platform import mac_ver
from re import S


# name = "小明"
# age = 19
# print(f"大家好，我叫{name}，今年{age}岁,明年我就{age+1}岁了")



# user = input("请输入一个整数：")



# print('howdy' in ['hello','hi','howdy','heyas'])
# spam = ['hello', 'hi', 'howdy', 'heyas']
# print('cat' in spam)
# print('howdy' not in spam)
# print('cat' not in spam)



# my_pets = ['Zophie', 'Pooka', 'Fat-tail']
# print('Enter a pet name:')
# name = input()
# if name not in my_pets:
#     print('I do not have a pet named ' + name)
# else:
#     print(name + ' is my pet.')



# cat = ['fat', 'gray', 'loud']
# size = cat[0]
# color = cat[1]
# disposition = cat[2]
# print(size)
# print(color)
# print(disposition)

# cat = ['fat', 'gray', 'loud']
# size, color, disposition = cat
# print(size)



# supplies = ['pens', 'staplers', 'flamethrowers', 'binders']
# for index, item in enumerate(supplies):
#     print('Index ' + str(index) + ' in supplies is: ' + item)



# import random
# pets = ['Dog', 'Cat', 'Moose']
# print(random.choice(pets))


# spam = 42
# spam = spam + 1
# print(spam)


# spam = 42
# spam += 1
# print(spam)



# spam = 'hello.'
# spam += 'world!'
# print(spam)

# bacon = ['Zophie']
# bacon *= 3
# print(bacon)




# append()   insert()      
# spam = ['cat', 'dog', 'bat']
# spam.append('moose')
# print(spam)

# spam = ['cat', 'dog', 'bat']
# spam.insert(1, 'chicken')
# print(spam)




# egg = 'hello'
# print(egg.upper('world'))
# Traceback (most recent call last):
#   File "<python-input-0>", line 1, in <module>
#     eggs.append('world')
# AttributeError: 'str' object has no attribute 'append'





# bacon = 42
# bacon.insert(1, 'world')
# Traceback (most recent call last):
#   File "<python-input-0>", line 1, in <module>
#     bacon.insert(1, 'world')
# AttributeError: 'int' object has no attribute 'insert'




# spam = ['cat', 'bat', 'rat', 'elephant']
# spam.remove('bat')
# print(spam)


# spam = ['cat', 'bat', 'rat', 'elephant']
# spam.remove('chicken')



# spam = ['cat', 'bat', 'rat', 'cat', 'hat', 'cat']
# spam.remove('cat')
# print(spam)


# spam = [2, 5, 3.14, 1, -7]
# spam.sort()
# print(spam)


# spam = ['Ants', 'Cats', 'Dogs', 'Badgers', 'Elephants']
# spam.sort()
# print(spam)



# spam = ['a', 'z', 'A', 'Z']
# spam.sort(key = str.lower)
# print(spam)



# spam = ['cat', 'dog', 'moose']
# spam.reverse()
# print(spam)




# n = int(input("请输入一个整数: "))
# print(f"平方: {n ** 2}")
# print(f"立方: {n ** 3}")


# print(7/2, type(7/2))
# print(7//2, type(7//2))
# print(7%2, type(7%2))
# print(2**10, type(2**10))
# print(10==10.0, type(10==10.0))


# leap_year = int(input("请输入一个年份: "))
# if (leap_year % 4 == 0 and leap_year % 100 != 0) or leap_year % 400 == 0:
#     print(f"{leap_year}是闰年")
# else:
#     print(f"{leap_year} 不是闰年")



# year = int(input("请输入一个年份: "))
# if (year % 4 == 0 and year %100 !=0) or year % 400 ==0:
#     print(f"{year}，是闰年")
# else:
#     print(f"{year}，不是闰年")


# total = float(input("请输入成绩(0~100):"))
# if 90 <= total <= 100:
#      print("优秀")
# elif 80 <= total <= 100:
#      print("良好")
# elif 70 <= total < 80:
#      print("中等")
# elif 60 <= total <70:
#      print("及格")
# elif 0 <= total < 60:
#      print("不及格")    
# else:
#     not (0 <= total <= 100)
#     print("成绩无效")
   


# total = float(input("请输入成绩(0~100):"))
# if not (0 <= total <= 100):
#     print("成绩无效") 
# elif total >= 90:
#     print("优秀")
# elif total >= 80:
#     print("良好")
# elif total >= 70:
#     print("中等")
# elif total >= 60:
#     print("及格")
# else:
#     print("不及格")
# 
# 
# 
# 


# stature = float(input("请输入身高(m):"))
# weight = float(input("请输入体重(kg):"))
# bmi = weight / stature ** 2
# if bmi < 18.5:
#     print("偏瘦")
# elif 18.5 < bmi <= 23.9:
#     print("正常")
# elif 24 < bmi <= 27.9:
#     print("超重")
# elif bmi >= 28:
#     print("肥胖")
# else:
#     print("非常肥胖")
    


# height = float(input("身高(米): "))
# weight = float(input("体重(公斤): "))
# bmi = weight / height ** 2
# print(f"你的 BMI 是: {bmi:.1f}")

# if bmi < 18.5:
#     print("偏瘦")
# elif bmi < 24:
#     print("正常")
# elif bmi < 28:
#     print("偏胖")
# else:
#     print("肥胖")



# count = 0
# for i in range(1,101):
#     if i % 3 == 0 and i % 5 != 0:
#         print(i, end="\t")
#         count += 1
#         if count % 5 == 0:
#             print()  # 每 5 个换一行





# for i in range(1, 10):
#     for j in range(1, i + 1):
#         print(f"{j} x {i} = {j * i}", end="\t")
#     print()  




# answer = 42
# count = 0
# while True:
#     guess = float(input("猜猜看是多少？"))
#     count += 1
#     if guess > answer:
#         print("猜大了")
#     elif guess < answer:
#         print("猜小了")
#     else:
#         print("恭喜你，猜对了！")
#         print(f"你一共猜了 {count} 次")
#         break
    



# answer = 42
# count = 0
# while True:
#     guess = int(input("猜猜看是多少？"))
#     count += 1
#     if guess > answer:
#         print("猜大了")
#     elif guess < answer:
#         print("猜小了")
#     else:
#         print("恭喜你，猜对了！")
#         print(f"你一共猜了 {count} 次")
#         break




# scores = [88, 92, 75, 60, 100, 45, 83]
# # print(len(scores))
# # print(max(scores))
# # print(min(scores))
# # print(sum(scores) / len(scores))
# # print(scores[1:4])
# scores[5] = 70
# print(scores)



# scores = [88, 92, 75, 60, 100, 45, 83]

# print(len(scores))                    # 7
# print(max(scores), min(scores))       # 100 45
# print(f"{sum(scores) / len(scores):.1f}")  # 77.6
# print(scores[1:4])                    # [92, 75, 60]
# scores.append(70)
# scores[scores.index(45)] = 55
# print(scores)  # [88, 92, 75, 60, 100, 55, 83, 70]



# import math
# def is_prime(n: int) -> bool:
#     if n < 2:
#         return False
#     # 只需要检查到 sqrt(n)，因为因子是成对出现的
#     for i in range(2, int(n ** 0.5) + 1):
#         if n % i == 0:
#             return False
#     return True





# my_cat = {'size': 'fat', 'color': 'gray', 'age': 17}
# print(my_cat['size'])
# My cat has ' + my_cat['color'] + ' fur.'



# birthdays = {'Alice': 'Apr 1', 'Bob': 'Dec 12', 'Carol': 'Mar 4'}

# while True:
#     print('Enter a name: (blank to quit)')
#     name = input()
#     if name == '':
#         break

#     if name in birthdays:
#         print(birthdays[name] + ' is the birthday of ' + name)
#     else:
#         print('I do not have birthday information for ' + name)
#         print('What is their birthday?')
#         bday = input()
#         birthdays[name] = bday
#         print('Birthday database updated.')





# spam = {'color': 'red', 'age': 42}
# for v in spam.values():
#         print(v)

# for k in spam.keys():
#     print(k)

# 'color' in spam.keys()
# 'age' not in spam.keys()

# 'red' in spam.values()

# for i in spam.items():
#         print(i)



# spam = {'color': 'red', 'age': 42}
# print(spam.keys())  # Returns a list-like dict_keys value
# print(list(spam.keys()))  # Returns an actual list value




# message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
# count = {}

# for character in message:
#     count.setdefault(character, 0) 
#     count[character] = count[character] + 1 

# print(count)




# import sys, copy

# STARTING_PIECES = {'a8': 'bR', 'b8': 'bN', 'c8': 'bB', 'd8': 'bQ',
# 'e8': 'bK', 'f8': 'bB', 'g8': 'bN', 'h8': 'bR', 'a7': 'bP', 'b7': 'bP',
# 'c7': 'bP', 'd7': 'bP', 'e7': 'bP', 'f7': 'bP', 'g7': 'bP', 'h7': 'bP',
# 'a1': 'wR', 'b1': 'wN', 'c1': 'wB', 'd1': 'wQ', 'e1': 'wK', 'f1': 'wB',
# 'g1': 'wN', 'h1': 'wR', 'a2': 'wP', 'b2': 'wP', 'c2': 'wP', 'd2': 'wP',
# 'e2': 'wP', 'f2': 'wP', 'g2': 'wP', 'h2': 'wP'}


# BOARD_TEMPLATE = """
#     a    b    c    d    e    f    g    h
#    ____ ____ ____ ____ ____ ____ ____ ____
#   ||||||    ||||||    ||||||    ||||||    |
# 8 ||{}|| {} ||{}|| {} ||{}|| {} ||{}|| {} |
#   ||||||____||||||____||||||____||||||____|
#   |    ||||||    ||||||    ||||||    ||||||
# 7 | {} ||{}|| {} ||{}|| {} ||{}|| {} ||{}||
#   |____||||||____||||||____||||||____||||||
#   ||||||    ||||||    ||||||    ||||||    |
# 6 ||{}|| {} ||{}|| {} ||{}|| {} ||{}|| {} |
#   ||||||____||||||____||||||____||||||____|
#   |    ||||||    ||||||    ||||||    ||||||
# 5 | {} ||{}|| {} ||{}|| {} ||{}|| {} ||{}||
#   |____||||||____||||||____||||||____||||||
#   ||||||    ||||||    ||||||    ||||||    |
# 4 ||{}|| {} ||{}|| {} ||{}|| {} ||{}|| {} |
#   ||||||____||||||____||||||____||||||____|
#   |    ||||||    ||||||    ||||||    ||||||
# 3 | {} ||{}|| {} ||{}|| {} ||{}|| {} ||{}||
#   |____||||||____||||||____||||||____||||||
#   ||||||    ||||||    ||||||    ||||||    |
# 2 ||{}|| {} ||{}|| {} ||{}|| {} ||{}|| {} |
#   ||||||____||||||____||||||____||||||____|
#   |    ||||||    ||||||    ||||||    ||||||
# 1 | {} ||{}|| {} ||{}|| {} ||{}|| {} ||{}||
#   |____||||||____||||||____||||||____||||||
# """
# WHITE_SQUARE = '||'
# BLACK_SQUARE = '  '

# def print_chessboard(board):
#     squares = []
#     is_white_square = True
#     for y in '87654321':
#         for x in 'abcdefgh':
#             #print(x, y, is_white_square)  # DEBUG: Show coordinates
#             if x + y in board.keys():
#                 squares.append(board[x + y])
#             else:
#                 if is_white_square:
#                     squares.append(WHITE_SQUARE)
#                 else:
#                     squares.append(BLACK_SQUARE)
#             is_white_square = not is_white_square
#         is_white_square = not is_white_square

#     print(BOARD_TEMPLATE.format(*squares))


# print('Interactive Chessboard')
# print('by Al Sweigart al@inventwithpython.com')
# print()
# print('Pieces:')
# print('  w - White, b - Black')
# print('  P - Pawn, N - Knight, B - Bishop, R - Rook, Q - Queen, K - King')
# print('Commands:')
# print('  move e2 e4 - Moves the piece at e2 to e4')
# print('  remove e2 - Removes the piece at e2')
# print('  set e2 wP - Sets square e2 to a white pawn')
# print('  reset - Resets pieces back to their starting squares')
# print('  clear - Clears the entire board')
# print('  fill wP - Fills entire board with white pawns.')
# print('  quit - Quits the program')


# main_board = copy.copy(STARTING_PIECES)
# while True:
#     print_chessboard(main_board)
#     response = input('> ').split()

#     if response[0] == 'move':
#         main_board[response[2]] = main_board[response[1]]
#         del main_board[response[1]]

#     elif response[0] == 'remove':
#         del main_board[response[1]]

#     elif response[0] == 'set':
#         main_board[response[1]] = response[2]

#     elif response[0] == 'reset':
#         main_board = copy.copy(STARTING_PIECES)

#     elif response[0] == 'clear':
#         main_board = {}

#     elif response[0] == 'fill':
#         for y in '87654321':
#             for x in 'abcdefgh':
#                 main_board[x + y] = response[1]

#     elif response[0] == 'quit':
#         sys.exit()




# all_guests = {'Alice': {'apples': 5, 'pretzels': 12},
#               'Bob': {'ham sandwiches': 3, 'apples': 2},
#               'Carol': {'cups': 3, 'apple pies': 1}}

# def total_brought(guests, item):
#     num_brought = 0
#     for k, v in guests.items():
#         num_brought = num_brought + v.get(item, 0)
#     return num_brought

# print('Number of things being brought:')
# print(' - Apples         ' + str(total_brought(all_guests, 'apples')))
# print(' - Cups           ' + str(total_brought(all_guests, 'cups')))
# print(' - Cakes          ' + str(total_brought(all_guests, 'cakes')))
# print(' - Ham Sandwiches ' + str(total_brought(all_guests, 'ham sandwiches')))
# print(' - Apple Pies     ' + str(total_brought(all_guests, 'apple pies')))


# spam = 'Say hi to Bob\'s mother.'
# print(spam)



# print("Hello there!\nHow are you?\nI\'m doing fine.")


# print(r'The file is in C:\Users\Alice\Desktop')


# print('Hello...\n\n...world!')
# print(r'Hello...\n\n...world!')  # With a raw string



# print('''Dear Alice,

# Can you feed Eve's cat this weekend?

# Sincerely,
# Bob''')




# print("Dear Alice,\n\nCan you feed Eve's cat this weekend?\n\nSincerely,\nBob")




# """This is a test Python program.
# Witten by Al Sweigart al@inventwithpython.com

# This program was designed for Python 3, not Python 2.
# """

# def say_hello():
#     """This function prints Hello.
#     It does not retrurn anything."""
#     print('Hello!')



# print('Hello' in 'Hello, World')
# print('Hello' in 'Hello')



# name = 'AI'
# age = 4000
# print('Hello, my name is ' + name + '. I am ' + str(age) + ' years old.')
# print('In ten years I will be ' + str(age + 10))



# name = 'Al'
# age = 4000
# print('My name is %s. I am %s years old.' % (name, age))




# print('How are you?')
# feeling = input()
# if feeling.lower() == 'great':
#     print('I feel great too.')
# else:
#     print('I hope the rest of your day is good.')


# Enter your age:
# forty two
# Please enter a number for your age.
# Enter your age:
# 42
# Select a new password (letters and numbers only):
# secr3t!
# Passwords can only have letters and numbers.
# Select a new password (letters and numbers only):
# secr3t




# def is_phone_number(text):
#     if len(text) != 12:
#         return False
#     for i in range(0, 3):
#         if not text[i].isdecimal():
#             return False
#     if text[3] != '-':
#         return False
#     for i in range(4, 7):
#         if not text[i].isdecimal():
#             return False
#     if text[7] != '-':
#         return False
#     for i in range(8, 12):
#         if not text[i].isdecimal():
#             return False
#     return True


# print('Is 415-555-4242 a phone number?', is_phone_number('415-555-4242'))
# print(is_phone_number('415-555-4242 '))
# print('Is Moshi moshi a phone number?', is_phone_number('Moshi moshi'))
# print(is_phone_number('Moshi moshi'))




# message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'
# for i in range(len(message)):
#     segment = message[i:i+12]
#     if is_phone_number(segment):
#         print('Phone number found: ' + segment)
# print('Done')




# import re
# phone_num_pattern_obj = re.compile(r'\d{3}-\d{3}-\d{4}')
# match_obj = phone_num_pattern_obj.search('My number is 415-555-4242.')
# print(match_obj.group())




# from pathlib import Path
# print(Path('spam', 'bacon', 'eggs'))
# print(str(Path('spam', 'bacon', 'eggs')))



# from pathlib import Path
# my_files = ['accounts.txt', 'details.csv', 'invite.docx']
# for filename in my_files:
#         print(Path(r'C:\Users\Al', filename))




# import os
# os.chdir('C:\ThisFolderDoesNotExist')
# print(os.chdir('C:\ThisFolderDoesNotExist'))



# import os
# print(os.makedirs('C:\\delicious\\walnut\\waffles'))



# from path import Path
# Path(r'C:\Users\AI\spam').mkdir()


# from pathlib import Path

# print(Path.cwd())


# from pathlib import Path
# print('my\relative\path')



# from pathlib import Path
# p = Path('C:\Users\AI\spam,tet')
# print(p.anchor)



# bacon_file = open('bacon.txt', 'w', encoding='UTF-8')   
# print(bacon_file.write('Hello, world!\n'))



# file_obj = open('data.txt', 'w', encoding='utf-8')
# file_obj.write('Hello, world!')
# file_obj.close()
# file_obj = open('data.txt', encoding='utf-8')
# content = file_obj.read()
# file_obj.close()




# import shelve
# shelf_file = shelve.open('mydata')
#  shelf_file['cats'] = ['Zophie', 'Pooka', 'Simon']
# shelf_file.close()



# randomQuizGenerator.py - Creates quizzes with questions and answers in
# random order, along with the answer key

# import random

# # The quiz data. Keys are states and values are their capitals.
# capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona':
# 'Phoenix', 'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado':
# 'Denver', 'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida':
# 'Tallahassee', 'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise',
# 'Illinois': 'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines',
# 'Kansas': 'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge',
# 'Maine': 'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston',
# 'Michigan': 'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson',
# 'Missouri': 'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln',
# 'Nevada': 'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton',
# 'New Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh',
# 'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
# 'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
# 'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
# 'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
# 'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'West
# Virginia':'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

# # Generate 35 quiz files.
#    for quiz_num in range(35):
#     # TODO: Create the quiz and answer key files.

#     # TODO: Write out the header for the quiz.

#     # TODO: Shuffle the order of the states.

#     # TODO: Loop through all 50 states, making a question for each.




# import shutil
# from pathlib import Path
# h = Path.home
# shutil.copy(h / 'spam/file1.txt', h)




# import shutil 
# from pathlib import Path
# h = Path.home()
# shutil.copytree(h / 'spam',h / 'spam_backup')



# import shutil
# form pathlib import Path
# h = Path.home()
# (h / 'spam2').mkdir()
# shutil.move(h / 'spam/file1.txt', h / 'spam2')




# shutil.move(h / 'spam/filel.txt',h / 'spam2/new_name.txt')



# import os, random, time, sys

# TOP    = chr(9600)  # Character 9600 is '▀'
# BOTTOM = chr(9604)  # Character 9604 is '▄'
# FULL   = chr(9608)  # Character 9608 is '█'

# # Set the snowstorm density to the command line argument:
# DENSITY = 4  # Default snow density is 4%
# if len(sys.argv) > 1:
#     DENSITY = int(sys.argv[1])

# def clear():
#     os.system('cls' if os.name == 'nt' else 'clear')

# while True:
#     clear()  # Clear the terminal window.

#     # Loop over each row and column:
#     for y in range(20):
#         for x in range(40):
#             if random.randint(0, 99) < DENSITY:
#                 # Print snow:
#                 print(random.choice([TOP, BOTTOM]), end='')
#             else:
#                 # Print empty space:
#                 print(' ', end='')
#         print()  # Print a newline.

#     # Print the snow-covered ground:
#     print(FULL * 40 + '\n' + FULL * 40)
#     print('(Ctrl-C to stop.)')

#     time.sleep(0.2)  # Pause for a bit.



# name = "小明"
# score = 92.5678

# print(f"{name} 考了 {score} 分")
# print(f"{name} 考了 {score:.1f} 分")    
# print(f"{name} 考了 {score:.0f} 分")




# import re

# LINE = "=" * 60

# def title(n, text):
#     print("\n" + LINE)
#     print(f"{n}. {text}")
#     print(LINE)


# class car:

# import datetime
# birthday = datetime.date(1999, 10, 31)
# print(birthday.year)    




# class WizCoin:
#     def __init__(self,galleons, sickles, knuts):
#       """Create a new WizCoin object with galleons, sickles, and knuts."""
#       self.galleons = galleons
#       self.sickles = sickles
#       self.knuts = knuts
#       # NOTE: __init__() methods NEVER have a return statement.
#     def value(self):
#       """The value (in knuts) of all the coins in this WizCoin object."""
#       return (self.galleons * 17 * 29) + (self.sickles * 29) + (self.knuts)
#     def weightInGrams(self):
#         """Returns the weight of the coins in grams."""
#       return (self.galleons * 31.103) + (sefl.sickles * 11,34) + (self.knuts * 5.0)





# import wizconin

# 1 purse = wizcoin.wizconin(2, 5, 99)
# print(purse)
# print('G:', purse.galleons, 's:', purse.sickles, 'K:', purse.knuts)
# print('Total value:', purse.value())
# print('weight:', purse.weightingrams(),'grams')

# print()

# 2 coinjar = wizcoin.wizcoin(13, 0, 0)
# print(coinjar)
# print('G:', coinjar.galleons, 'S:', coinjar.sickles, 'K:',coinjar.knuts)
# print('Total value:', coinjar.value())
# print('weight:', coinjar.weightinGrams(), 'grams')



# class ParentClass:
#     def __init__(self, name):
#       print('Hello, world')

# class ChildClass(ParentClass):
#   def someNewMethod(self):
#     print('ParentClass object don\'t have this method')

# class GrandChildClass(ChildClass):
#   def someNewMethod(self):
#     print('only GrandChildClass object have this method')

# print('Create a ParentClass object and call its methods:')
# parent = ParentClass()
# parent.printHello()

# print('Create a ChildClass object and call its methods:')
# child = ChildClass()
# child.printHello()
# child.someNewMethod()

# print('Create a GrandChildClass object and call its methods:')
# grandchild = GrandChildClass()
# grandchild.printHello()
# grandchild.someNewMethod()
# grandchild.anotherNewMethod()

# print('An error:')
# parent.someNewMethod()



# class ParentClass:
#     def printHello(self):
#         print('Hello, world!')

# class ChildClass(ParentClass):
#     def someNewMethod(self):
#         print('ParentClass objects don\'t have this method.')

# class GrandchildClass(ChildClass):
#     def anotherNewMethod(self):
#         print('Only GrandchildClass objects have this method.')

# print('Create a ParentClass object and call its methods:')
# parent = ParentClass()
# parent.printHello()

# print('Create a ChildClass object and call its methods:')
# child = ChildClass()
# child.printHello()
# child.someNewMethod()

# print('Create a GrandchildClass object and call its methods:')
# grandchild = GrandchildClass()
# grandchild.printHello()
# grandchild.someNewMethod()
# grandchild.anotherNewMethod()

# print('An error:')
# parent.someNewMethod()



# class MiniBoard(TTTBoard):
#     def getBoardStr(self):
#         """Return a tiny text-representation of the board."""
#         # Change blank spaces to a '.'
#         for space in ALL_SPACES:
#             if self._spaces[space] == BLANK:
#                 self._spaces[space] = '.'

#         boardStr = f'''
#           {self._spaces['1']}{self._spaces['2']}{self._spaces['3']} 123
#           {self._spaces['4']}{self._spaces['5']}{self._spaces['6']} 456
#           {self._spaces['7']}{self._spaces['8']}{self._spaces['9']} 789'''

#         # Change '.' back to blank spaces.
#         for space in ALL_SPACES:
#             if self._spaces[space] == '.':
#                 self._spaces[space] = BLA




# class ParentClass:
#     """父类：只有一个 printHello() 方法。"""

#     def printHello(self) -> None:
#         """打印问候语。"""
#         print('Hello, world!')


# class ChildClass(ParentClass):
#     """子类：继承 printHello()，并新增 someNewMethod()。"""

#     def someNewMethod(self) -> None:
#         """这是子类（及其子类）独有的方法。"""
#         print('ParentClass objects don\'t have this method.')


# class GrandchildClass(ChildClass):
#     """孙类：继承上面两个方法，并新增 anotherNewMethod()。"""

#     def anotherNewMethod(self) -> None:
#         """这是孙类独有的方法。"""
#         print('Only GrandchildClass objects have this method.')


# print('Create a ParentClass object and call its methods:')
# parent: ParentClass = ParentClass()
# parent.printHello()

# print('Create a ChildClass object and call its methods:')
# child: ChildClass = ChildClass()
# child.printHello()
# child.someNewMethod()

# print('Create a GrandchildClass object and call its methods:')
# grandchild: GrandchildClass = GrandchildClass()
# grandchild.printHello()
# grandchild.someNewMethod()
# grandchild.anotherNewMethod()

# # 继承是单向的：父类对象没有子类新增的方法。
# # 这里故意调用一次，用 try/except 把 AttributeError 接住并打印出来，
# # 既保留了"看错误长什么样"的教学目的，又不会让整个程序崩在半路。
# print('An error:')
# try:
#     parent.someNewMethod()  # type: ignore[attr-defined]
# except AttributeError as err:
#     print(f'AttributeError: {err}')




# class HintBoard(TTTBoard):
#     def getBoardStr(self):
#         """Return a text-representation of the board with hints."""
#           boardStr = super().getBoardStr() # Call getBoardStr() in TTTBoard.

#         xCanWin = False
#         oCanWin = False
#           originalSpaces = self._spaces # Backup _spaces.
#         for space in ALL_SPACES: # Check each space:
#             # Simulate X moving on this space:
#             self._spaces = copy.copy(originalSpaces)
#             if self._spaces[space] == BLANK:
#                 self._spaces[space] = X
#             if self.isWinner(X):
#                 xCanWin = True
#             # Simulate O moving on this space:
#               self._spaces = copy.copy(originalSpaces)
#             if self._spaces[space] == BLANK:
#                 self._spaces[space] = O
#             if self.isWinner(O):
#                 oCanWin = True
#         if xCanWin:
#             boardStr += '\nX can win in one more move.'
#         if oCanWin:
#             boardStr += '\nO can win in one more move.'
#         self._spaces = originalSpaces
#         return boardStr





# --snip--
#     def __iadd__(self, other):
#         """Add the amounts in another WizCoin object to this object."""
#     if not isinstance(other, WizCoin):
#             raise NotImplemented

#     # We modify the 'self' object in-place:
#     self.galleons += other.galleons
#     self.sickles += other.sickles
#     self.knuts += other.knuts
#     return self 

#     def __imul__(self, other):
#         """Multiply the amounts in this WizCoin object by a factor."""
#         by a non-negative integer amoumt."
#         if not isinstance(other, int):
#         if other < 0:
#             raise WizConinException("cannot multiply with negative integers.")

#         # The WizCoin class creates mutable objects, so do NOT create a
#         # new object like this commented-out code:
#         #return WizCoin(self.galleons * other, self.sickles * other, self.knuts * other)

#         # We modify the `self` object in-place:
#         self.galleons *= other
#         self.sickles *= other
#         self.knuts *= other
#         return self  # In-place dunder methods almost always return self.





# class Student:
#     def __init__(self, name, score):
#         self.name = name
#         self.score = score


#     def show_score(self):
#         print(f"{self.name} has a score of {self.score}")

#     def add_bonus(self, bonus):
#         self.score += bonus


# s = Student("Tom", 85)
# s.show_score()
# s.add_bonus(5)




# class Student:
#     def __init__(self, name):
#         self.name = name
    
#     def hello(self):
#         print(f"我是 {self.name}")


# a = Student("小明")
# b = Student("小红")

# a.hello()
# b.hello()

# class Student:
#     def __init__(self, name, score=0):   
#         self.score = score

# s1 = Student("小明", 85)    
# s2 = Student("小红")         




# class Counter:
#     species = "计数器家族"

#     def __init__(self, name):
#         self.name = name
#         self.count = 0




# class Temperature:
#     unit = "摄氏度"

#     def __init__(self, value):
#         self.value = value

#     def show(self):
#         print(f"{self.value} {self.unit}")

#     @classmethod
#     def set_unit(cls, value, unit):
#         cls.unit = unit
    
#     @staticmethod
#     def is_valid(v):
#         return -273.15 <= v <= 1000

# Temperature.set_unit(100, "华氏度")
# Temperature(25).show()
# print(Temperature.is_valid(-500))




# class  Student:
#     unit1 = "分"
#     unit2 = "岁"
#     unit3 = "米"
#     unit4 = "千克"

#     def __init__(self, name, score, age, stature, weight):
#        self.name = name
#        self.score = score
#        self.age = age
#        self.stature = staturt
#        self.weight = weight

#     def show(self):
#         print(f"{self.name}的分数是{self.score}{self.unit1},年龄是{self.age}{self.unit2},身高是{self.stature}{self.unit3},体重是{self.weight}{self.unit4}")
    
#     @classmethod
#     def set_unit(cls, unit1, unit2, unit3, unit4):
#         cls.unit1 = unit1
#         cls.unit2 = unit2
#         cls.unit3 = unit3
#         cls.unit4 = unit4

#     @staticmethod
#     def is_valid(age, stature, weight):
#         return 0 <= age <= 100 and 0 <= stature <= 2.5 and 0 <= weight <= 200

# Student.set_unit("分", "岁", "米", "千克")
# Student("小明”, 90, 18, 1.75, 60).show()
# print(Student.is_valid(18, 1.75, 60)) 

# class Student:
#     # 类属性：默认单位
#     unit1: str = "分"
#     unit2: str = "岁"
#     unit3: str = "米"
#     unit4: str = "千克"

#     def __init__(self, name: str, score: float, age: int, stature: float, weight: float) -> None:
#         self.name = name
#         self.score = score
#         self.age = age
#         self.stature = stature
#         self.weight = weight

#     def show(self) -> None:
#         print(f"{self.name}的分数是{self.score}{self.unit1},"
#               f"年龄是{self.age}{self.unit2},"
#               f"身高是{self.stature}{self.unit3},"
#               f"体重是{self.weight}{self.unit4}")

#     @classmethod
#     def set_unit(cls, unit1: str, unit2: str, unit3: str, unit4: str) -> None:
#         cls.unit1 = unit1
#         cls.unit2 = unit2
#         cls.unit3 = unit3
#         cls.unit4 = unit4

#     @staticmethod
#     def is_valid(age: int, stature: float, weight: float) -> bool:
#         return 0 < age <= 100 and 0 < stature <= 2.5 and 0 < weight <= 200


# Student.set_unit(unit1="分", unit2="岁", unit3="米", unit4="千克")
# Student("小明", 90, 18, 1.75, 60).show()
# print(Student.is_valid(age=18, stature=1.75, weight=60))

# class Student:
#     unit1 = "分"
#     unit2 = "岁"
#     unit3 = "米"
#     unit4 = "千克"

#     def __init__(self, name, score, age, stature, weight):
#        self.name = name
#        self.score = score
#        self.age = age
#        self.stature = stature
#        self.weight = weight

#     def show(self):
#         print(f"{self.name}的分数是{self.score}{self.unit1},"
#               f"年龄是{self.age}{self.unit2},"
#               f"身高是{self.stature}{self.unit3},"
#               f"体重是{self.weight}{self.unit4}")
    
#     @classmethod
#     def set_unit(cls, unit1, unit2, unit3, unit4):
#         cls.unit1 = unit1
#         cls.unit2 = unit2
#         cls.unit3 = unit3
#         cls.unit4 = unit4

#     @staticmethod
#     def is_valid(age, stature, weight):
#         return 0 <= age <= 100 and 0 <= stature <= 2.5 and 0 <= weight <= 200

# Student.set_unit("分", "岁", "米", "千克")
# Student("小明", 90, 18, 1.75, 60).show()
# print(Student.is_valid(18, 1.75, 60)) 



# class Student:
#     def __init__(self, name, score = 0):
#         self.name = name
#         self.score = score
#         print(f"[出生登记] {self.name}创建完成")

# s1 = Student("小明", 85)
# s2 = Student("小红")





# a = 10/3
# print(a)
# print(f'a的值是{a}')
# print(f'a的值是{a:.2f}')
# print(f'{a:.2f}')
# print(f'{a:.0f}')
# print(f'{a:.1f}')

# s = '苹果 香蕉 橘子'
# lst = s.split()
# print(lst)

# a = 3.14
# print(int(a))




# s = "10"                    
# a = int(s)                   
# b = float(s)
# print(a, b)



# num = 20
# text = str(num)
# print(text)


# f = open("test.txt", "r", encoding = "utf-8")
# date = f.read()
# f.close()



