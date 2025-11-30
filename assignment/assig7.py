# 1. List Comprehension (Basics)
"""
1. Given the list
nums = [2,5,7,10,13]
create a new list containing the cube of each number using list comprehension.
2. from the list 
nums =[3,8,12,15,,18,21]
create a new list that contains only the numbers divisible by 3.

3. Given words =["apple", "cat", "banana", "car", "dog"]
create a list that contains the words that do not starts with 'c'.


""" 
# nums = [2,5,7,10,13]
# cubes = [num**3 for num in nums]
# print(cubes)

# nums = [3,8,12,15,18,21]
# divisible_by_3 = [num for num in nums if num % 3 == 0]
# print(divisible_by_3)

# words =["apple", "cat", "banana", "car", "dog"]
# not_starting_with_c = [word for word in words if word[0] != 'c']
# print(not_starting_with_c)

# 2. Dictionary Comprehension
"""
4. Given the dictionary 
scores = {1:55, 2:80, 3:40, 4:90}
create a new dictionary containing only the items where the score is above 60.
5. convert this dictionary into a reverse dictionary(swap key->value)
colors ={
    1: "red",
    2: "blue",
    3: "green"
    }
    
"""

# scores = {
#     1:55, 
#     2:80, 
#     3:40, 
#     4:90
#     }
# above_60 = {key: value for key, value in scores.items() if value > 60}
# print(above_60)

# colors = {
#     1: "red",
#      2: "blue",
#      3: "green"
#      }
    
# reverse_colors = {value: key for key, value in colors.items()}
# print(reverse_colors) 

# 3. Exception handling"
"""
6. write program that:

    takes a number from the user
    tries to convert it to an integer
    if the user enters something invalid, print 
    "Invalid input! Please enter number"

7. write a program that :
    ask the user for two numbers
    tries to divide them
    handles:
        ValueError -> when input is not a number
        ZeroDivisionError -> when denominator is 0
        Exception -> when something else goes wrong

    print "Division Successful!" inside the else block

"""

num = input("Enter a number:")
try:
    num = int(num)
    print(num)
except ValueError:
    print("Invalid input! Please enter number")

# try:
#     num1 = int(input("Enter a number:"))
#     num2 = int(input("Enter another number:"))
#     result = num1 / num2
#     print(result)
# except ValueError:
#     print("Invalid input! Please enter number")
# except ZeroDivisionError:
#     print("Cannot divide by zero")
# except Exception:
#     print("Something went wrong")

# OR,


# try:
#     # Ask the user for two numbers
#     num1 = float(input("Enter the first number: "))
#     num2 = float(input("Enter the second number: "))

#     # Try to divide them
#     result = num1 / num2

# except ValueError:
#     print("Error: Please enter valid numeric values.")

# except ZeroDivisionError:
#     print("Error: Cannot divide by zero.")

# except Exception as e:
#     print("An unexpected error occurred:", e)

# else:
#     # Runs only if no exception happens
#     print("Division Successful!")
#     print("Result:", result)

# finally:
#     print("Program completed.")


# 4. File Handling
""""
File Handling examples (with code)

# 1. Writing to a file (w mode)
creates the file if it does not exist
overwrites the file if it already exists

# EXAMPLE 1:
file = open("hello.txt", "w")
file.write("Hello Students!")
file.close()

#EXAMPLE 2:
file = open("fruits.txt","w")
file.write("Apple/n")
file.write("Banana/n")
file.write("Mango/n")
file.close()

"""

""""
2. Reading from a file(R mode)
file must exist
used to read data from a file

EXAMPLE 3:

file = open("hello.txt", "r")
content = file.read()
print(content)
file.close()
 
EXAMPLE 4: Read line by line

file = open("fruits.txt", "r")
for line in file:
    print(line.strip()) #strip() removes the newline character(\n)
    file.close()
    

EXAMPLE 5: Read all lines into a list

file = open("fruits.txt", "r)
lines = file.readlines()
print(lines)
file.close()

"""

"""
3. Appending to a file (a mode)

Adds new content at the end
Does not delete previous data

EXAMPLE 6:

file = open("hello.txt", "a")
file.write("Hello Students!\n")
file.close()

"""

"""
4. Using with open() (BEst practice)
 Automatically closes the file
 Prevents mistakes like forgetting close()

 EXAMPLE 7: Writing with WIth

 with open("city.txt", "w") as f:
 f.write("Kathmandu\n")
 f.write("Pokhara\n")
 f.write("Biratnagar\n")

 EXAMPLE 8: Reading with with

 with open("city.txt", "r") as f:
 content = f.read()
 print(content)

"""


"""
5. Example: Reading Numbers And Doing Something with them

Assume numbers.txt contains

10
20
30
40
50

EXAMPLE 9: Read numbers and calculate sum

with open("numbers.txt", "r") as f:
    total = 0
    for line in f:
    total += int(line.strip())

print("Total:", total)  

"""

"""
# 6. Example : Write user input to a file

EXAMPLE 10:  Ask the user for 3 names and save them 

    with open("names.txt", "w") as f:
    for i in range(3):
    name = input("Enter name:")
    f.write(name + "\n")
"""

"""
7. Example : Read a file safely (with Exception Handling)
EXAMPLE 11: Handle file not found error


try:
    with open("unknown.txt", "r") as f:
    content = f.read()
    print(content)

except FileNotFoundError:
    print("File not found")
"""