
            # operators in Python
            # Relational Operators in Python
# take two numbers from user and perform all relational operations
# num1=int(input("Enter first number: "))
# num2=int(input("Enter second number: "))
# print(num1<num2)
# print(num1>num2)
# print(num1<=num2)   
# print(num1>=num2)
# print(num1==num2)
# print(num1!=num2)
# ====================================================

# take age from user and check various conditions
# age=int(input("Enter your age: "))
# print(age>18)
# print(age<18)
# print(age==18)
# ====================================================


# take marks from user and check if marks lies between 20 and 40
# marks=int(input("Enter your marks: "))
# print(20<marks<40)
# ====================================================

            # Logical Operators in Python(and, or, not)
# enter two numbers and perform logical operations
# a=int(input("Enter first number: "))
# b=int(input("Enter second number: "))
# print((a>0) and (b>0)) #compares if both a and b are greater than 0 and only true values is returned when both conditions are true
# print((a>0) or (b>0)) #compares if either a or b is greater than 0 and true value is returned when at least one condition is true
# print(not(a>0)) #reverses the boolean value of the condition
#not(5>0) => not True => False
#not 5 is greater than 0 => not True => False
# =====================================================

# input marks and full marks and check if marks lies between 0 and full marks
# marks=int(input("Enter your marks: "))
# FM=int(input("Enter full marks: "))
# print((marks<0 or marks>FM))
# =====================================================

# demonstration of logical operators
# print(5>3 and 2<4) #True and True => True
# print(5<2 or 10>3) #False or True => True
# print(not 7==7) #not True => False
# =====================================================


            # String Operators in Python
# concatenation of two strings(+ operator)
# first_name=input("Enter your first name: ")
# last_name=input("Enter your last name: ")
# print(first_name + last_name) #concatenation of two strings
# print(first_name + " " + last_name) #concatenation of two strings with space in between
# =====================================================


# repetition of string(* operator)
# name=input("Enter your name:")
# n = int(input("Enter how many times to repeat your name:"))
# print((name + " ") * n)
#repeats the string n times
# give space while repeating the string
# =====================================================

            # Length Operator in Python (len())
# word length of a string
# name=input("Enter your name:")
# print(len(name)) #gives the length of the string
# =====================================================

# check if length of string is greater than 5
# name=input("Enter your name:")
# print(len(name)>5) #checks if length of string is greater than 5

# =====================================================

        # Membership Operators in Python (in, not in)

# check if a word is present in a string
# text=input("Enter a string: ")
# word=input("Enter a word to search: ")
# print(word in text) #checks if word is present in text
# print(word not in text) #checks if word is not present in text
# ====================================================

# print("a" in 'apple') #True
# print("b" in 'apple') #False
# print("c" not in 'apple') #True 
# print("ram" in "ramhari") #True
# print("hari" not in "ramhari") #False
# print("hi" in "hello") #False
# print("hari" in "ram hari") #True
# =====================================================


# Identity operators in Python (is, is not)
# a=5
# b=5
# print(a is b) #True, because both a and b point to same memory location
# print(a is not b) #False, because both a and b point to same memory location
# c=[1,2,3]
# d=[1,2,6]
# print(c is d) #False, because both c and d point to different memory locations
# print(c is not d) #True, because both c and d point to different memory locations
# =====================================================


# identity operator with None
# a=None
# b=None
# print(a is not b) #False, because both a and b point to same memory location
# print(a is b) #True, because both a and b point to same memory location
# ====================================================

# identity operator with strings
# name1="python"
# name2="python"
# print(name1 is name2) #True, because both name1 and name2 point to same memory location
# print(name1 is not name2) #False, because both name1 and name2 point to same memory location    
# ====================================================

# identity operator with lists
# list1=[1,2,3]
# list2=[1,2,6]
# print(list1 is list2) #False, because both list1 and list2 point to different memory locations
# print(list1 is not list2) #True, because both list1 and list2 point to different memory locations   
# ====================================================

# Variable naming practices in python
# 5 valid and 5 invalid variable names
# StudentName="John" #Camel Case
# student_name="Doe" #Snake Case
# studentName="Alice" #Pascal Case
# _student="Eve" #Valid variable name (starts with underscore)
# studentName1="Frank" #Valid variable name (contains number at the end)
# 1st_student="Bob" #Invalid variable name (starts with a number)
# student-name="Charlie" #Invalid variable name (contains hyphen)
# student name="David" #Invalid variable name (contains space)
# student$name="Grace" #Invalid variable name (contains special character)
# 1+Student_name="Hannah" #Invalid variable name (contains operator)
# or_student="Ivy" #Invalid variable name (uses reserved keyword)
# ====================================================


# Rename the following variables to meaningful names:
# a = 20
# b = 30
# c = a+b
# print(c)

# math_marks = 20
# science_marks = 30
# total_marks = (math_marks + science_marks)
# print(total_marks)
#==============================================


# try writing snake_case
# student_name = "sangita"
# total_marks = 60
# number_of_students = 50
# full_name ="ram hari"
# english_marks = 80
# print(student_name)
# print(total_marks)
# ==============================

# try assigning reserved words as variable names (eg. or=5) and observe the syntax error
# or = 5 #syntax error as it is Or is reserved variable of python
# print(or)

# =============================


# check the conditions and observes the result
print(10>5 and 5 <10) #True and True => True
print(10==5 or 5 <10) #False or True => True
print(not 3 > 2) #not True => False
print("a" in "data") #True
print(len("python") >=6) #True



