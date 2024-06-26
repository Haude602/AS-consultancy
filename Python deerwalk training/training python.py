# # int,float, bool, str, list, tuple, set, dict
# my_list = ['A', 2, 4.0, True]
# print (my_list)
# my_list.pop(0) #pop deletes the element based on value whereas remove deletes based on element
# print(my_list)

# my_list.sort()
# print(my_list)
# print(my_list.index(4.0))
# print(my_list.count(2))
# print(my_list.count(True))

# my_list.reverse()
# print(my_list)

# your_list = my_list.copy()
# print(your_list)

# my_tuple = (1,2,3,4,5,6)
# print(my_tuple)
# print(my_list.count(1))
# print(my_tuple.index(2))

# my_set = {1,2,3,4,4,5,6,'ram'}
# print(my_set)
# new_set = my_set.copy()
# my_set.clear()
# print(my_set)
# print(new_set)
# print(my_set)

# my_dict = {
#     'one' : (1,1,1,1),
#     'two' : 2
# }
# print(my_dict)
# print(my_dict.items())
# print(my_dict.keys())
# print(my_dict.values())

# for a, b in my_dict.items():
#     print(a,b)

# for item in my_dict.items( ):
#     a, b = item
#     print(a,b)








# Conditional Statement

# age = 18
# if age < 18:
#     print('you are underaged')
# else:
#     print('you are adult')

# age = 21
# if age == 0:
#     print('yet to born')
# elif 0 < age <= 5:
#     print('you are a child')
# elif 5< age <=20:
#     print('you are young')
# else:
#     print('you are adult')

# num = 40
# if num< 50:
#     print('less than 50')
# elif num < 80:
#     print('less than 70')
# else:
#     print('number looks good')

    

# loop , iteration , repeatation , recursion

# i = 0
# while i < 4:
#     print('Ram')
#     i+=1 # Or i = i + 1

# for item in ('book','copy','rough'):
#     print(item)

# for item in ('bookcopy'):
#     print(item)

# for item in 'book':
#     print(item)

# for item in range (20):
#     print(item)

# for item in range (20,30):
#     print(item)

# for item in range (20,30, 2):
#     print(item)
#while loop is used when we have idea about how many times we want to run
#the loop whereas for loop is used blindly

# #function    #repeated useful piece  of code is written inside function

# def greet():
#     print('Hi! nice to meet you')
#     print('how are you')
#     print( 'how was your day')
#     print('did you have your lunch')

# greet()
# print('yoyo')
# greet()

# #string concatenation

# print('ram'+ 'Shyam')
# print('ram', 'shyam')


# name= ('david')
# print (f'the name of this boy is {name}')
# print('the name of this boy is',name)
# print ('the name of this boy is'+ name)# for this same nature of code is required integer cha bhane integer, string cha bhane string

# name= 'David'
# age= 40

# print(f'the mane of this boy is {name} and age is{age}')  #formatted string

# print('the name of this boy is'+name, 'and age is', age)

 
# def greet(name):
#     print('hello'+ name,'there')
#     print(f'Welcome{name} home')
#     print('heyhey')
#     print("it's dinner time", name)

# greet('ram')
# print('hellohello')
# greet('hari')

# def greet (name='ram', surname= 'oli'):
#     print(f'hello {name} {surname} there')
#     print('welcome home')
# greet()
# greet('ram')
# greet('shyam', 'shrestha')  
# name= "hari"
# age= 8
# print(f"he's either{name.upper()} or age is {age}+teen")
# print("He's either",name.upper(),'or age is',str(age)+"+teen")

# print('''It's a very "sunny" day''')

# Parameters 

# # escape sequence (\)
# print('It\'s a very \"Sunny\" day')

# def greet(name):
#     print(name)
# greet('ram')

# def greet(name):
#     return(name)
# yo = greet
# print(yo('ram'))

# class mammal:
#     def cow(self):
#         print(' cow is a mammal')
#     def goat(self):
#         print('goat is also a mammal')

# animal = mammal()
# animal1 = mammal()
# # animal.cow()
# # animal.goat()

# # class classroom:
# #     def student(self):
# #         print('student reads in class')
    
# #     def teacher(self):
# #         print('teacher teaches in class')
# # person1 = classroom()
# # person1.student()
# # person1.teacher()

# # person2= classroom()
# # person2.student()
# # person2.teacher()

# # weight = 70
# # age = 4

# # try:
# #     if weight/age < 4:
# #         print('your weight is normal')
# #     # else:
# #     #     print('your weeight is over')
# # except ZeroDivisionError:
# #     print('age cant be zero')
# # print('ram')
# # print('shyam')

# # import pandas as pd
# # df = pd.read_csv('C:/Users/pravi/Downloads/archive/music.csv')
# # print(df)

# # df = pd.read_csv('C:/Users/pravi/Downloads/archive/music.csv')
# # print(df)
# # print(df.shape)
# # print(df.describe())
# # print(df.agg())

# #type conversion  (scrapping: robots.txt)
# # import datetime
# # current_date= datetime
# # birth_year = input("birth year:")
# # year = int(birth_year)
# # age = 2024 - year
# # # print(age)

# # A= [1,2,3,4,5,6]
# # B=[4,5,6,7,8]
# # A.append(B)
# # print(A)

# # print (int("101", 2)) #or input (0b101)
# # print (int("101", 8))
# # print(bin(20))

# # print(1==1.0) #== checks only value
# # print(1 is 1.0)# is also checks datatypes
# # print('ram' is 'ram')
# # print([] is []) #every time we create a list, it gets formed in separate memory location
# # # so list is not equals to list while we use is

# # print(5%2)
# # print(5/2)
# # print(5//2)
# import math
# # print(math.ceil(2.1))
# # print(math.floor(2.1))
# # print(math.ceil(2.9))
# # print(math.floor(2.9))

# # print(round(0.5))
# # print(round(1.5))
# # print(round(2.5))
# # print(round(3.5))

# # print(math.sqrt(4))

# # my_dict= {
# #     1 : 'one'
# #     2 : 'two'
# # }
# # print(a,b)


# list =[1,2,4,7,9, 8, 10]
# print(list)
# list.append(50)
# print(list)
# list.remove(2)
# print(list)
# list.extend([20,50])
# print(list)
# list.insert(1,5)
# print(list)
# list.index(5)
# print(list.index(5))
# list1=list.copy()
# # print(list1)
# # print(list1.pop(0))
# list1.pop(3)
# print(list1)
# print(list1.index(4))
# print(list1.count(4))

# list1.reverse()
# print(list1)
# list1.sort()
# print(list1)

# wow={1,2,3,4}#set is unordered collection of items hence doesnot support indexing
# print(wow[0])

# my_dict= {
#     'name': 'Ram',
#     'age': 20,
#     'town': 'chabel',
#     'is_male': True
# }
# print(my_dict.items())

# for item in my_dict.items():
#     print(item)

# for item in my_dict.keys():
#     print(item)

# for item in my_dict.keys():
#     print(item)

# for item in my_dict.values():
#     print(item)

# for key,value in my_dict.items():
#     print(key,value)

# for item in my_dict.items():
#     k,v = item
#     print(k,v)

# weight= int(input('please enter your weight:'))
# unit= input('Enter K for Kg(s) or L for Lb(s):')
# if unit.upper()== 'K':
#     Converted = weight/0.45
#     print(f'you are {Converted} pounds')
# elif unit. upper()=='L':
#     converted= weight*0.45
#     print(f'you are {converted} Kilos')
# else:
#     print("please insert'K' for kilos and 'L' for Pound")
    # print('\n')

# guessing game
# # 
# secret_number = 5
# guess_count = 0
# guess_limit = 3
# while guess_count < guess_limit:
#     guess = int(input('Please enter your number: '))
#     guess_count += 1
#     if guess == secret_number:
#         print('you won')
#     else:
#         if guess_count != 3:
#             print('Try again')

# else:
#     print('you failed')

# is_friend= True

# if is_friend:
#     print('message allowed')
# else:
#     print('message not allowed')

# def greet():
#     print('hello')
#     print('welcome to python class')
#     print("don't miss the class")
# greet()

# def calculate_triangle(b,h):
#     return 1/2*b*h
# print(float(calculate_triangle(3,4)))

# def calculate_square(n):
#     ''' Ram! this function calculates the square of the value'''
#     print('hello')
# calculate_square


# OOP: Object Oriented Programming

# def super_func(*a):
#     return sum(a)
# print(super_func(1,2,3,4,5,6))

def Super_func(*a,**b):
    total = 0
    for item in b.values():
        total += item           #total = total+ item
    return sum(a)+ total
print(Super_func(1,2,3,4,5,6, num1 = 4, num2 = 40, num3 = 10))









