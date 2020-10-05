#one line comment
"""This is
multiline comment

#Print------------------------------------------------------------------------------------------------------------------
print("Hello, World!", "One more line", end="new line")

print("\nHello there this is escape sequence character \n Thank you ")

#variables and Srings---------------------------------------------------------------------------------------------------
var1 ="5"
var2 = 5
var3 = 5.5
var4 = "6"
var5="Hi There "
print("var1",var2,var3,"var4")
print(type(var1))
print(var2 + var3)
print(var1 + var4)

print(int(var1) + int(var2))
print(10*(var5))

print(5*var2)
print(5*str(var2))

#Getting Input from user------------------------------------------------------------------------------------------------
print("Enter Your number")
number = input()
print("your number",number)
print("you enter number * 10 is:",10 * int(number))


print("Enter First Number")
num1 = input()
print("Enter Second Number")
num2 = input()
print("The Addition of two numbers is:",int(num1) + int(num2))

#StringFunctions--------------------------------------------------------------------------------------------------------
print(str1[:19])
print(str1[0:7:2]) #devided by two is printed
print(len(str1))
print(str1[-7:-1])

str1 = "Python programming is awesome"

print(str1.endswith("some"))
print(str1.count("a"))
print(str1.find("pro"))
print(str1.capitalize())
print(str1.upper())
print(str1.replace("is","are"))

#List-------------------------------------------------------------------------------------------------------------------
grocery = ['chana','dal','chocolate','rice','fruits','vegitables' ]
print(grocery)
print(grocery[5])
num = [1,2,3,5,40,9,0]
#print(num[6] = 6)
print(num.append(5))
print(num.insert(1,-1))
print(num.remove(5))
print(num)
print(num[2])
num.sort()
print(num)
#num.reverse()
print(num)
print(num[::4])
tup = (1,2,3,5,4)#immutable
print(tup)
print(type(tup))
#print(tup.inerst(1,5))
a=5
b=8
print(a,b)
a , b =  b ,a
print(a,b)

dict ={}
print(type(dict))

dictfood = {"caty":"Jammun","john":"salad","rectil":"cake",
"koly":{"B":"salad","L":"Rice","D":"Pizza"}}
print(dictfood)
print(dictfood["koly"]["B"])

dictfood[5] = "Meggie"
print(dictfood)
dcopy = dictfood
print(dcopy)
del dcopy[5]
print(dictfood)
print(dcopy)
print(dcopy.keys())
print(dcopy.items())
print(dictfood["caty"])

#create the dictionary with user input-----------------------------------------------------------------------------------

userdict  = {"1":"Namy","2":"Mariya","3":"jems","4":"partine","5":"kethrine"}

print("Enter the key number of user from 1-5")
num1 = input()

print("Here is the name of user:",userdict[num1])


s = set()
print(type(s))
set_list = set([1,2,3,4,5,6])
s.add(5)
s.add(55)
s.remove(55)
print(s)

var1 = 6
var2 = 56
var3 = int(input())

if var3 > var2:
    print("Greater")
elif var3 == var2:
    print("Equal")
else:
    print("Leser")


mylist = [5,3,6]
print(55 in mylist)
if 5 in mylist:
    print("Yes")


list1 = ['Maria','6','10','caty','john','stephy','15','caqty','99','2']
for data in list1:
    if str(data).isnumeric():
    print(data)


#whileloop--------------------------------------------------------------------------------------------------------------
i = 1
j = 1
while i<=5:
    print("While Loop")
    while j<=4:
        print("Python")
        j = j+1
    i = i+1
num= 0
while(num < 10):
     print(num)
     num = num +1

for numb in range(1,11):
    print(numb)


num = 0
while(True):
    if num+1<5:
        num = num +1
        continue
    print(num+1, end=" ")
    if(num == 45):
        break
    num = num +1

while(True):
    print("Enter The number")
    num1 = int(input())
    if(num1 >= 100):
            print("Congrats , You enter number grater than 100")
    else:
        continue

#Operators in python----------------------------------------------------------------------------------------------------
#Arithmetic
#assignment
#Comparisoin
#logical
#identity
#membership
#bitwize

#Arithmetic
print(5+3)
print(5-3)
print(5*3)
print(5//3)
print(5**3)
print(5%3)

#assignment
x = 3
print(x)
x += 10
print(x)

#Comparisoin
i = 10
print(i == 5)

#logical
a = True
b = False
print(a or b)

#identity
a=10
b=12
print(a is b)

#membership
list1 = [2,3,4,6,5]
print(34 not in list1)

#bitwize
#00 01 10 11
print(0|1)

#Shorthand IfElse-------------------------------------------------------------------------------------------------------
a = int(input("Enter A "))
b = int(input("Enter B "))

if a>b: print("A is greater")
else: print("B is greater")


#Fuctions---------------------------------------------------------------------------------------------------------------
#def func1(a,b):
 #   print("Addition ",a+b)
#func1(1,2)

#def func2(a,b):
    #print("Average ", (a+b)/2 )
#func2(6,6)

def func3(a,b):
#Enter stings b\w 3 "
    avg = (a+b)/3
    return avg

avgg = func3(2,9)
print(avgg)
print(func3.__doc__)

#ExeptionHandling-------------------------------------------------------------------------------------------------------
print("Enter 2 numbers")
num1 = input()
num2 = input()
try:
    print("No's are",int(num1)+int(num2))
except Exception as e:
    print(e)

# File Io Basics
"r" -Open file for reade
"w" -Open file for write
"x" -Crete file is not exist
"a" -append or add more content to a file
"t" -text mode
"b" -binary mode
"+" -for read and write

# file read--------------------------------------    --------------------------------------------------------------------
# you have to ceate txt file for open file program in this case file name is basics.txt create your own
filee = open("basics.txt")
content = filee.read()
print(content)
filee.close()

# File writing-----------------------------------------------------------------------------------------------------------
op = open("basics.txt","a")
op.write("Hello this is file writing")
op.write("This is append")
op.close()


# More about files-------------------------------------------------------------------------------------------------------
op = open("basics.txt")
# For knowing position of pointer
print(op.tell())
#For reseting pointer
op.seek()
op.close()

# File open using with block
with open("basics.txt") as op:
    re = op.read(4)
    print(re)

#Local and Global Concept------------------------------------------------------------------------------------------------
num = 20 #GLobal
def func(m):
    #num = 30   #Local
    print(num)
func("Local")
print(num)

#Global KeyWord---------------------------------------------------------------------------------------------------------
def func1(m):
    num = 500
    print(m,num)
func1("Local Variable")
print(num)

#if i use local variable here then it cause error that's why we are going to define the variable as global
def func1(m):
    global num
    num = 500
    print(m,num)
func1("Local Variable")
print(num)

# External & Built In Modules-------------------------------------------------------------------------------------------
import random
random_num = random.randint(0,5)
print(random_num)

# F strings-------------------------------------------------------------------------------------------------------------
name = input("Enter Your Name ")
department = input("Enter Department Name ")
greetings = f"Welcome {name} in Department Of {department} Enginerring"
print(greetings)

# *args and **kwargs------------------------------------------------------------------------------------------------------
def data(*args):
    for d in args:
        print(d)
list = ["caty","jen","tomy"]
data(*list)

# Time Module-----------------------------------------------------------------------------------------------------------
import time
tm = time.time()
for i in range(4):
    print("Counting time")
print("Time Of Ecxecution",time.time() - tm,"Seconds")

localtime = time.asctime(time.localtime(time.time()))
print(localtime)

#if__name__==__main__----create another py file and in another file call this fun and import this file------------------
def printni(string):
    return "this is my python"
def add(num1,num2):
    return num1+num2
if __name__ == '__main__':
    print(printni("python"))
    num = add(10, 20)
    print(num)

# joinfunction----------------------------------------------------------------------------------------------------------
list=["kety","fiber","rogh","locy"]
name= " and ".join(list)
print(name)

# map,filter and reduce---------------------------------------------------------------------------------------------------
# map
def sqr(n):
    return n*n
numbers = ["4","7","8","56"]
numbers = list(map(int, numbers))
number = list(map(sqr, numbers))
num = numbers[0]+numbers[1]
print(num)
print(number)

# map-ex
def square(num):
    return num*num
def cube(num):
    return num*num*num
func = [square,cube]
for i in range(10):
    value = list(map(lambda x:x(i),func))
print(value)

#Filter
list1 = [1,2,3,4,5,6,9]
def is_greater(num):
    return num>3
gr = list(filter(is_greater,list1))
print(gr)

# Reduce
from functools import reduce
ery 30min eydone
# Exersise - ex.mp3
# ls = [1,2,3,4,5]
# data = reduce(lambda x,y:x+y,ls)
# print(data)

# Decorators--------------------------------------------------------------------------------------------------
def dec(func1):
    def nowexec():
        print("Exectuing Now!")
        func1()
        print("Executed ")
    return nowexec
def whoisme():
    print("Me is Me")
whoisme = dec(whoisme)   
whoisme()


# Object Oriented Programming Concepts Starts From Here---------------------------------------------------------------------------------------------
# Uses Dry Concepts - Do not repeate yourself

class Student:
    pass
Nidhi = Student()
Nidhi.name = "Nidhi"
Nidhi.surname = "Makdani"
print(Nidhi.name)

#Instance And Class

class Students:
    std = 12
    subjects = ['maths','science','physics','cprogramming']
    div = "B"
    teachers = ['ms.caty','mr.john']
    pass

Nidhi = Students()
print(Students.__dict__)
print(Students.subjects)



# self & init cunstroctors

#self
class Students:
    div = "B"
    def printdetails(self):
        return f"Name is {self.name}, Standard is {self.std}"
Nidhi = Students()
Nidhi.name = "Nidhi"
Nidhi.std = 12
print(Nidhi.printdetails())
print(Nidhi.div)

#init (Constructor)
class Students:
    div = "B"
    def __init__(self,namee):
        self.name = namee
    def printdetails(self):
        return f"Name is {self.name}."
Nidhi = Students("Nidhi")
print(Nidhi.name)

# Class Method
class Students:
    div = "B"
    def __init__(self,namee):
        self.name = namee

    def printdetails(self):
        return f"Name is {self.name}."

    @classmethod
    def change_div(cls,newdiv):
        cls.div = newdiv

Nidhi = Students("Nidhi")
Nidhi.change_div("X")
print(Nidhi.div)

#Class Method as alternative COnstructor

class Employee:
    no_of_leaves = 10

    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetails(self):
        return f"The Name is {self.name}. Salary is {self.salary} and role is {self.role}"

    @classmethod
    def change_leaves(cls, newleaves):
        cls.no_of_leaves = newleaves

    @classmethod
    def from_dash(cls, string):
        # params = string.split("-")
        # print(params)
        # return cls(params[0], params[1], params[2])
        return cls(*string.split("-"))


Nidhi = Employee("Nidhi", 555, "Instructor")
John = Employee("John", 755, "Student")
Priya = Employee.from_dash("Prioya-480-Student")

print(John.no_of_leaves)
John.change_leaves(45)
print(Nidhi.no_of_leaves)


#Static Methods in Python
class Employee:
    no_of_leaves = 8

    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetails(self):
        return f"The Name is {self.name}. Salary is {self.salary} and role is {self.role}"

    @classmethod
    def change_leaves(cls, newleaves):
        cls.no_of_leaves = newleaves

    @classmethod
    def from_dash(cls, string):
        return cls(*string.split("-"))

    @staticmethod
    def printgood(string):
        print("This is good " + string)

Nidhi = Employee("Nidhi", 255, "Instructor")
John = Employee("John", 455, "Student")
Kery = Employee.from_dash("Carry-480-Student")

Employee.printgood("John")


#Static Methods in Python

class Employee:
    no_of_leaves = 8

    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetails(self):
        return f"The Name is {self.name}. Salary is {self.salary} and role is {self.role}"

    @classmethod
    def change_leaves(cls, newleaves):
        cls.no_of_leaves = newleaves

    @classmethod
    def from_dash(cls, string):
        return cls(*string.split("-"))

    @staticmethod
    def printgood(string):
        print("This is good " + string)


class Programmer(Employee):
    no_of_holiday = 56
    def __init__(self, aname, asalary):
        self.name = aname
        self.salary = asalary

    def printprog(self):
        return f"The Programmer's Name is {self.name}. Salary is {self.salary} and role is {self.role}.The languages are {self.languages}"

Nidhi = Employee("Nidhi", 255, "Instructor")
kety = Programmer("kety", 777)
print(kety.salary)

#************************************************Starting OOP**********************************************************
#Let'Cover all the concepts of OOP in Python--------------------------------------------------------------------------------------------------------------------------------------------
#Class- Design,Blurpeint
#Object - Real Entity
#Instance - Object is instance of class

#First We have to create design in any project same we create class first

class computer:
    #Attributes(Values)
    #Methods(Functions)
    def config(self):
        print("This is I5 machine")
comp1 = computer()
# print(type(comp1)) #Its class computer
comp1.config()


#Example
class Students:

    def computer(self):
        print("This student is from Computer Department")

    def it(self):
        print("This student is from IT Department")

    def auto(self):
        print("This student is from Automobile Department")

Nidhi = Students()
Payal = Students()
Gahena = Students()
Gopi = Students()

Nidhi.computer()
Payal.auto()


# Init method
class computer:

    def __init__(self,cpu,ram):
        #No need to call
        self.cpu = cpu
        self.ram = ram

    def config(self):
        print("Config is",self.cpu, self.ram)

comp1 = computer('i5',16)

comp1.config()

#Example

class student:

    def __init__(self,name,std,div,batch,marks):
        self.name = name
        self.std = std
        self.div = div
        self.batch = batch
        self.marks = marks

    def print_details(self):
        print("Details are",self.name,self.std,self.div,self.batch,self.marks)

Nidhi = student('Nidhi',12,'A','Morning',96)

Nidhi.print_details()

# Constructor and self
#Self IS point the function to appropriate location it's accourding using which instance you call

# Types of Variables
# 1 instance variable 
# 2 class variable

class car:
    weels = 4 # class
    def __init__(self):
        self.mil = 10
        self.comp = "BMW" #instance variable
c1= car()
c2= car()

print(c1.comp,c2.mil,c1.weels)

# Diffrent types of method
# instance
# class
# static

class students:

    school = 'RSV'

    def __init__(self,m1,m2,m3):
        self.m1 = m1 #instance method
        self.m2 = m2        
        self.m3 = m3
    def avg(self):
        return (self.m1 + self.m2 + self.m3)/2
  
    @classmethod
    def getschool(cls): #class method
        return cls.school

    @staticmethod
    def info():
        print("This is student info class")

s1 = students(54,56,45)
s2 = students(69,96,65)

students.info()
print(s1.avg())

# Inner class
class student:

    def __init__(self,name,rollno):
        self.name = name
        self.rollno = rollno
        self.lap = self.laptop()

    def show(self):
        print(self.name, self.rollno)   
        self.lap.show()

    class laptop:

        def __init__(self):
            self.brand = 'HP'
            self.cpu = '15'

        def show(self):
            print(self.brand,self.cpu)

s1 = student("Nidhi",5)
s2 = student("Kety",6)

s1.show()

# Inheritance 
#Single Inheritence
class A: #Super Class

    def func_a(self):
        print("This is class A")

class B(A):  #Subclass

    def func_b(self):
        print("This is class B")

b1 = B()
b1.func_b()
b1.func_a()


#Multilevel Inheritence
class A: #Super Class

    def func_a(self):
        print("This is class A")

class B(A):  #Subclass

    def func_b(self):
        print("This is class B")

class C(B):  #Subclass

    def func_c(self):
        print("This is class C")

c1 = C()
c1.func_a()
c1.func_b()
c1.func_c()

#Multiple Inheritence
class A: #Super Class

    def func_a(self):
        print("This is class A")

class B:  #Subclass

    def func_b(self):
        print("This is class B")

class C(A,B):  #Subclass

    def func_c(self):
        print("This is class C")

c1 = C()
c1.func_a()
c1.func_b()
c1.func_c()

#Constructor #method resolution order
class A: #Super Class

    def __init__(self):
        print("In A init")

    def func_a(self):
        print("This is class A")

class B:  #Subclass

    def __init__(self):
        print("In B init")
        super().__init__()

    def func_b(self):
        print("This is class B")

class C(A,B):  #Subclass

    def __init__(self):
        print("In C init")
        super().__init__()

c1 = C()



# Ploymorohism
# one thing multiple form
#WAYS of polymorphism
# Duck typing 
# operator overloading
# method overriding
# method overloading

# Duck typing #operator

class pycharm:
    def execute(self):
        print("complie")
        print("Run")

class grab:
    def execute(self):
        print("complie")
        print("Run")
        print("Spell check")

class laptop:
    def code(self,ide):
        ide.execute()

ide = grab()
lab1 = laptop()
lab1.code(ide)


# operator overloading
class student:
    
    def __init__(self,m1,m2):
        self.m1 =m1
        self.m2 =m2
    def __add__(self,other):
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2
        s3 = student(m1,m2)

        return s3
s1 = student(56,56)
s2 = student(62,56)

s3 = s1+s2
print(s3.m1)

#method overloading
class student:
    
    def __init__(self,m1,m2):
        self.m1 =m1
        self.m2 =m2
    def sum(self,a=None,b=None,c=None):
        s=0
        if a!= None and b!=None and c!=None:
            s = a+b+c
        elif a != None and b!=None
            s= a+b 
        else:
            s=a
        return s
s1 = student(56,56)      
print(s1.sum(6,4)) 

# Method Overriding
class A:
    def show(self):
        print("In class A")
class B(A):
    def show(self):
        print("In class B")
    pass
a1 = B()
a1.show()

#Abstract class

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def printarea(self):
        return 0

class Rectangle(Shape):
    type = "Rectangle"
    sides = 4
    def __init__(self):
        self.length = 6
        self.breadth = 7

    def printarea(self):
        return self.length * self.breadth

rect1 = Rectangle()
print(rect1.printarea())

#************************************************Complete OOP**********************************************************

# Generators-----------------------------------------------------------------------------------------------------------------------------------------------------
# Iterable __iter__() or __getiteam__()
# Iterator  __next__()
# Iteration

def genr(n):
    for i in range(n):
        yield i #generator

g = genr(5)
print(g)
print(g.__next__())
print(g.__next__())
print(g.__next__())
print(g.__next__())
print(g.__next__())
print(g.__next__()) #COZ ERROR

name = "Nidhi"
ier = iter(name)
print(ier.__next__())
print(ier.__next__())
print(ier.__next__())
print(ier.__next__())
print(ier.__next__())
print(ier.__next__()) #COZ ERROR

# Comprehensions --------------------------------------------------------------------------------------------------

#List Comprehensions 
lst = [i for i in range(100) if i%3 == 0]
print(lst)

#Dictionary Comprehensions 
dict1 = {i:f"item{i}" for i in range(101) if i%2==0}
print(dict1)

#Reverse Code
dicti = {i:f"item{i}" for i in range(5)}
dicti = {value:key for key,value in dicti.items()}
print(dicti)

# Set Comprehensions
num = {nm for nm in{"1","2","3","1","2","3","1"}}
print(num)

# Generator Comprehensions
evens = (ev for ev in range(100) if ev%2==0)
print(evens.__next__())
print(evens.__next__())
print(evens.__next__())


# using else with for loops------------------------------------------------------------------------------------------------

food = ["pasta","ghevar","laddu"]

for f in food:
    if f == "pizza": 
        break
else:
    print("Your item is not in List")


# Function Caching--------------------------------------------------------------------------------------------------
import time 
from functools import lru_cache

@lru_cache(maxsize=3)
def some_work(n):
    time.sleep(n)
    return n

if __name__ == "__main__":
    print("Running Some work")
    some_work(3)
    print("done.. calling again")
    some_work(3)
    some_work(6)#use last three calls
    some_work(5)
    some_work(5)
    print("called")

# Else and Finally in Try Except -----------------------------------------------------------------------------------------
f1 = open("basics.txt")
try:
    f = open('not.txt') #change it with valid txt and else will run
    
except Exception as e:
    print(e)

else: 
    print("Exept does not run")

finally:
    print("Run this")
    # f.close()
    f1.close()
print("Important Stuff")

# Coroutines----------------------------------------------------------------------------------
def searcher():
    import time
    #Consume 4 seconds
    book = "Book open"
    time.sleep(4)

    while True:
        text = (yield)
        if text in book:
            print("Text in BOOK")
        else:
            print("Not in BOOK")
   
search = searcher()
print("Search Started.....")
next(search)
search.send("Nidhi")
input("press any key")
search.send("Book")

# OS module-------------------------------------------------------------------------------------
#Remove One by One error and run
import os
# print(os.getcwd())
# os.chdir("C://")
# print(os.getcwd())
# print(os.listdir("D://"))
# os.mkdir("Nidhi")
# os.makedirs("Nidhi/Makdani")
# os.rename("basics.txt","basic.txt")
# os.rename("basic.txt","basics.txt")
# print(os.path.exists("D://"))
# print(os.path.isfile("D://"))
# print(os.path.isdir("D://"))
# Check all the Functions


# Request Module---------------------------------------------------------------------------------------------------------------------------
# import requests

# r = requests.get("https://requests.readthedocs.io/en/master/")
# print(r.text)

# url ="www.434.com"
# data ={"p1":4,"p2":5}
# data = {
#     "p1":4,
#     "p2":4
# }
# # r2 = request.post(url=url,data=data)
# #DONE MORE IN REQUEST


# json-------------------------------------------------------------------------------------------------

import json
data = '{"var1":"Nidhi", "var2":21}'
print(data)
parsed = json.loads(data)
print(type(parsed))

data2 = {
    "name": "Nidhi",
    "hoby": ['song', 'games', 'code'],
    "isbad": False
}
jscomp = json.dumps(data2)
print(jscomp)


# Pickle Module----------------------------------------------------------------------
# import pickle
# name = ["Nidhi","John","Carry"]
# str_file = "dta.pkl"
# file_object = open(str_file,'wb')
# pickle.dump(name,file_object)
# file_object.close()
# file_open = "dta.pkl"
# file_obj = open(file_open,'rb')
# name = pickle.load(file_obj)
# print(name)

# Regular Expression----------------------------------------------------------------------------------
import re
stri = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."

#TRY ALL FUNCTION

# pattern = re.compile(r'.')
# pattern = re.compile(r'.fass')
# pattern = re.compile(r'$text')
# pattern = re.compile(r'^lorem')
# pattern = re.compile(r'sum$')
# pattern = re.compile(r'sim*')
# op = pattern.finditer(stri)
# for output in op:
#     print(output)


# raise ---------------------------------------------------------------------------------------------

a = input()
b = input()
if int(b)==0:
    raise ZeroDivisionError("b is 0 so stopping the program")
print(f"Hello {a}")


# c = input("Enter your name")
# try:
#     print(a)
# except Exception as e:
#     if c =="nidhi":
#         raise ValueError("Already There")
#     print("Exception handled")


# is and == -------------------------------------------------------------------------------------------
# == means value equality
# is means reference equality 

a = 10
b = 10

if a == b:
    print("Values are same")

c = {"nidhi,makdani"}
print(c is a)

# Regular Expressions
import argparse
import sys

def calc(args):
    if args.o == 'add':
        return args.x + args.y

    elif args.o == 'mul':
        return args.x * args.y

    elif args.o == 'sub':
        return args.x - args.y

    elif args.o == 'div':
        return args.x / args.y

    else:
        return "Wrong Data......"

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--x', type=float, default=1.0,
                        help="First Number")

    parser.add_argument('--y', type=float, default=3.0,
                        help="Second number")

    parser.add_argument('--o', type=str, default="add",
                        help="This is a utility for calculation")

    args = parser.parse_args()
    sys.stdout.write(str(calc(args)))
"""

#Completed 
# Happy Learning
# Now Go For Projects
