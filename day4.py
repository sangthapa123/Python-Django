# Relational operators
# These operators compare two values and return a boolean result.
# <, >, <=, >=, ==, !=
# Example:
a = 10  
b = 20
print(a < b)   # True
print(a > b)   # False      
print(a <= b)  # True
print(a >= b)  # False
print(a == b)  # False
print(a != b)  # True
# =====================================================

# Logical operators
# These operators are used to combine conditional statements.
# and, or, not
# AND : Sabai true huda matrao true dincha
# OR  : Kunai ek true huda true dincha  
# NOT : True lai false ra false lai true banaucha
# Example:
x = 5
print(x > 0 and x < 10)  # True 

# 20-40 ->D
# print(20<english<40)
# englishmarks>20
# englishmarks<40
englishmarks = 35
print(englishmarks > 20 and englishmarks < 40)  # True # D
print(englishmarks > 40 and englishmarks < 60)  # False # F


# Rules for naming variables
# 1. Variable names must start with a letter (a-z, A-Z) or an underscore (_).
# eg: myVar, _1myVar

# 2. The rest of the variable name can contain letters, digits (0-9), or underscores.
# eg: myVar1, _my_Var2

# 3. Variable names are case-sensitive (e.g., myVar and myvar are different).
# eg: myVar, MyVar

# 4. Variable names cannot be the same as Python reserved keywords (e.g., if, else, while, etc.).
# eg: myVar, not if

# 5. Variable names should not contain spaces; use underscores (_) instead. 
# eg: my_var, myVar
# marks_of_student (snake_case) Conventionally used in Python
# marksOfStudent (camelCase) Commonly used in other programming languages like JavaScript, Java

# 6. Variable names should be descriptive to make the code more readable.
# eg: student_age, total_price

# 7. reserved keywords cannot be used as variable names
# eg: if, else, while, for, return, etc.
# or=5  # Invalid variable name because 'or' is a reserved keyword 
# =====================================================

# Example:
my_variable = 10    
anotherVariable = 20
_variable_name = 30
print(my_variable + anotherVariable + _variable_name)  # 60
# Invalid variable names (uncommenting these will cause errors):
# 1variable = 10      # Starts with a digit
# my-variable = 20   # Contains a hyphen
# if = 30            # Reserved keyword
# my variable = 40   # Contains a space
# =====================================================

# String operators
# +,

first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name + " "  # Concatenation
print(full_name)  # John Doe
print(full_name * 3)  # Repetition John Doe John Doe John Doe
# =====================================================

# LENGTH OPERATOR
# len() function returns the length of a string
first_name = "John"
# print(len(first_name))  # 4
no_of_characters = len(first_name)
print(no_of_characters)  # 4
# =====================================================

# Membership operators, (In, Not In)
# These operators test for membership in a sequence (like strings, lists, or tuples).
shareholders = ["Ram", "Shyam", "Hari", "Sita"]
print("Ram" in shareholders)       # True   
print("Gita" not in shareholders)  # True
print("Gita" in shareholders)     # False
# =====================================================


# string OPERATORS
# +CONCATENATION
# *REPETITION

# IDENTITY OPERATORS
# is, is not
# These operators compare the memory locations of two objects.
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x
print(x is z)      # True, because z references the same object as x
print(x is y)      # False, because x and y are different objects   
print(x is not y)  # True, because x and y are different objects
print(x is not z)  # False, because z references the same object as x
# =====================================================
# Example:
a = 5   
b = 5
print(a is b)      # True, because both refer to the same integer object
print(a is not b)  # False, because both refer to the same integer object   
# =====================================================

