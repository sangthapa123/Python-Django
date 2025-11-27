# A. Basic Conditionals (Simple)
# 1. print enter number either zero, negative or positive
# number = int(input("Enter a number: "))
# if number > 0:
#     print(f"{number} is a positive number.")
# elif number == 0:
#     print("The number is zero.")
# else:
#     print(f"{number} is a negative number.")

# 2. Age group classification(child(below 13), teen(13-17), adult(18 and above))
# age = int(input("Enter your age: "))    
# if age < 13:
#     print("You are a child.")
# elif age >= 13 and age< 18:
#     print("You are a teenager.")
# else:
#     print("You are an adult.")

# OR,

# age = int(input("Enter your age: "))
# if age < 13:
#     print("You are a child.")
# elif 13 <= age < 18:
#     print("You are a teenager.")
# else:
#     print("You are an adult.")

# 3. Temperature check. if temperature is 30 degree celsius or above its hot otherwise cold)
# temp = float(input("Enter the temperature in celsius:"))
# if temp > 30:
#     print("It's hot outside.😨")
# else:
#     print("It's cold outside.🥶")

# 4. Larger of two numbers
# ask user to enter two numbers and print which number is larger.
# number1 = int(input("Enter first numbers : "))
# number2 = int(input("Enter second number : "))
# if number1>number2:
#     print(f"{number1} is greater than {number2}")
# elif number1<number2:
#     print(f"{number1} is smaller than {number2}")
# else:
#     print("The numbers are equal")

# 5. Even And Odd numbers
# print whether the number is odd or even
# marks = int(input("Enter a number : "))
# if marks%2==0:
#     print(f"{marks} is even")
# else:
#     print(f"{marks} is odd")

# 6. Password Check
# if the entered password matches the predefined word "python", print"Access Granted", otherwise print "Access Denied".
# password = input("Enter the password : ")
# if password == "python":
#     print("Access Granted!")
# else:
#     print("Access Denied!")


# 7. Divisibility (Fizz/Buzz)
# if its divisible by 5 print Fizz or print buzz if divisible by 3. if divisible by both print both.
# number = int(input("Enter a number : "))

# if number%5==0 and number%3 == 0:
#     print("Fizz and Buzz")
# elif number%5==0:
#     print("Fizz")
# elif number%3==0:
#     print("Buzz")
# else:
#     print("Is not divided by 3 and 5")

# 8. Number in range
# check if it lies within the range 1 to 10(inclusive). Print whether it is in the insidse or outside range.
# number = int(input("Enter the number : "))
# if number > 1 and number <= 10:
#     print("The number lies inside the range")
# else:
#     print("The number lies outside the range")

# 9. Leap year
# Ask user for a year and check if it a leap year, using the simple rule, a year is leap if it is divisible by 4.

# year = int(input("Enter year :"))
# if year%4==0:
#     print("Leap year")
# else:
#     print("Not Leap year")

# 10. Grade based on marks
# Ask the user to enter their marks (out of 100). print the grade according to:
# 90 - 100 -> A
# 80 - 89  -> B
# 70 - 79  -> C
# Below 70 -> Fail

# marks = int(input("Enter your marks : "))
# if marks <= 100 and marks >90 :
#     print("Grade A")
# elif marks < 89 and marks > 80:
#     print("Grade B")
# elif marks < 79 and marks > 70:
#     print("Grade C")
# elif marks <= 70:
#     print("Fail")
# else:
#     print("Invalid marks")

#  B. Conditionals (Fun & Logical)
# 11. Favourite colour
# Ask user to enter color and if they entered "BLUE" print "Cool Choice" otherwise "Nice"

# color = input("Enter your favourite Color :")
# if color == "blue":
#     print("Wow! Cool Choice!😎")
# else:
#     print("Nice👌")

# 12. Name starting with A
# if the name begins with letter A print "Awesome name!", otherwise print "Nice name!"

# name = input("Enter your name :")
# if name.startswith("A") or name.startswith("a"):
#     print("Awesome name!")
# else:
#     print("Nice name!")

# 13. is number too big?
# ask user for a number, if it is greater than 100, print too big else print just right.

# number = int(input("Enter any number :"))
# if number >= 100 :
#     print("The number is too big")
# else:
#     print("Just right")

# 14. Equal numbers check
# ask user to enter two numbers and print "Twins" if both numbers are equal, else print "Different number"
# num1 = int(input("Enter first number :"))
# num2 = int(input("Enter second number :"))
# if num1 == num2:
#     print("Twinny.")
# else:
#     print("Different number.")

# 15. Height Eligibility
# ask user to enter their heights in CM, if it is above 180cm print "you can join the basketball team" else print "You may try chess"

# height = float(input("Enter your heights in cm : "))
# if height > 180 :
#     print("You can join the basketball team")
# else:
#     print("You may try chess")

# 16. Divisible by 2 and 3
# check the number if it is divisible by both 2 and 3 then print "special number"
# number = int(input("Enter any number :"))
# if number%2 == 0 and number%3 == 0:
#     print("Special number!")
# else:
#     print("Normal number!")

# 17. Check if character is a Vowel
# check either enter character is a vowel(a,e,i,o,u) then print "Vowel"
# char = input("Enter a single character :")
# if char in ['a','e','i','o','u'] :
#     print("The vowel character")
# else:
#     print("Normal character")

# 18. Speed limit Check
# enter speed limit. of the speed is more than 80km/h, print "overspeeding", else print "Safe Driving"
# speed = float(input("Enter your speed in : "))
# if speed > 80:
#     print("Overspeeding🤐")
# else:
#     print("Safe Drive🤞")

# 19. Check round number
# enter number and if its last number is 0 print"nice round number"

# number = int(input("Enter any number :"))
# if number % 10 == 0:
#     # 120/10 ==12
#     print("Nice round number")
# else:
#     print("Not a round number")

# 20. Check multiple
# ask user for two number and print whether the second number is a multiple of the first number.
# Eg1.
# numb1 = int(input("Enter first number :"))
# numb2 = int(input("Enter second number :"))
# if numb1 != 0 and numb2 % numb1 == 0:
#     print(f"{numb2} is a multiple of {numb1} ")
# else:
#     print(f"{numb2} is not a multiple of {numb2}")

# Eg2.
# num1 = int(input("Enter the first number: "))
# num2 = int(input("Enter the second number: "))

# if num2 / num1 == num2 // num1:
#     print(f"{num2} is a multiple of {num1}")
# else:
#     print(f"{num2} is not a multiple of {num1}")

# Eg3.

# num1 = int(input("Enter the first number: "))
# num2 = int(input("Enter the second number: "))

# # Check if the second number is a multiple of the first
# if num2 % num1 == 0:
#     print(f"{num2} is a multiple of {num1}")
# else:
#     print(f"{num2} is not a multiple of {num1}")

# 21. print number 1-10
# print all numbers from 1-10 using loop

# for i in range(1,11):
#     print(i)

# 22. Even number 1-20
# print all even numbers from 1-20(inclusive)

# for i in range(1, 21):
#     if i % 2 == 0:
#         print(i)


# 23. reverse counting
# print numbers from 10 to 1 using loop.

# for i in range(11,0,-1):
#     print(i)

# 24. print 1 to n
# ask the user for a number n, and print numbers from 1 to n.

# number = int(input("Enter n numbers :"))
# for i in range(1,number):
#     print(i)

# 25. multiplication table of 5
# using loop, print the multiplication table of 5(from 5x1 to 5x10)
# for n in range (1,11):
#     print(f"5x{n} = {5*n}")

# # 26. multiplication table of desired number
# number = int(input("Enter the number for table you want :"))
# for n in range (1,11):
#     print(f"{number}x{n} = {number*n}")

# 27. print hello 5 times

# for n in range(5):
#     print("Hello")


# 28. print characters of the word
# ask user for a word and print each word in new line

# name = input("Enter your name :")
# for char in name:
#     print(char)


# 29. numbers divisible by 3
# for i in range(1, 31):
#    if i % 3 == 0:
#     print(i)

# 30. sum of numbers 1 - 10
# sum = 0
# for i in range(1,10):
#     print(sum+i)

# LOOPS + CONDITIONALS(COMBINED  LOGIC)

# 31. Even numbers upto n 
# n = int(input("Enter n number :"))
# for i in range(2,n+1,2):
#         print(i)

# 32.squares of numbers
# print the square of each number from 1 to 10

# for i in range(1,11):
#     print(i**2)

# 33. count multiples of 4
# count how many numbers between 1 and 20 are divisible by 4 and print the count.

# for i in range(1,20):
#     if i % 4 == 0:
#         print(i)

# 34. numbers divisible by 2 and 5
# ask the user for n number and betn 1 to n that are divisible by 2 and 5.

# num = int(input("Enter n number :"))
# for i in range(1,num+1):
#     if i % 2==0 and i % 5 ==0:
#         print(i)


# 35. numbers ending with the 7
# print the all numbers betn 1 and 50 whose last digit is 7. 

# for i in range(1,50):
#     if i % 10 == 7:
#         print(i)


# 36. Multiple of 10
# print all of multiples of 10 between 1 and 200

# for i in range(1, 200):
#     if i % 10 == 0:
#         print(i)

# 37. boom for multiple of 3
# ask user for a number n. print all the numbers from 1 to n but whenever a number is divisible by 3, print BOOM instead of the number.

# num = int(input("Enter n number :"))
# for i in range(1, num):
#     if i % 3 == 0 :
#         print(f"{i} Boom")


# 38. sum of even numbers up to n
# ask the user for a number n, and calculate the sum of all numbers bet 1 and n

# num = int(input("Enter n number :"))
# sum = 0
# for i in range(num+1):
#     sum+=i
#     print(sum)

# 39. print python n times
# ask the user for n number and print python exactly n times

# numb = int(input("Enter the n number :"))
# for i in range(numb):
#     print("python")


# 40. product of 1-5
# using a loop, find the product of numbers from 1 to 5. (this is like factorial of 5) 

# product = 1
# for i in range(1, 6):
#     product *= i  # Multiply product by i in each iteration

# print("Product =", product)


# 41. 


# secret_number = 7  # Choose your secret number here

# while True:
#     guess = int(input("Guess the number: "))

#     if guess == secret_number:
#         print("🎉 Correct! You guessed the secret number!")
#         break
#     else:
#         print("❌ Wrong guess. Try again!")

# 42. Ask the user for a positive integer. Count how many digits the number has (e.g., 423 → 3 digits)

# num = input("Enter a positive integer: ")
 # Remove any leading + signs, just in case
# num = num.lstrip("+")
 # Count digits
# digit_count = len(num)

# print(f"The number {num} has {digit_count} digits.")

# 43. 

# num = int(input("Enter a number: "))

# # Handle sign
# sign = -1 if num < 0 else 1
# n = abs(num)

# # Step 1: Count digits
# temp = n
# digits = 0
# while temp > 0:
#     temp //= 10
#     digits += 1

# Step 2: Rebuild reversed number
# reversed_num = 0
# for i in range(digits):
#     last_digit = n % 10
#     reversed_num += last_digit * (10 ** (digits - i - 1))
#     n //= 10

# reversed_num *= sign  # restore sign

# print("Reversed number:", reversed_num)

# 44

# for i in range(1, 4):
#     for j in range(i):
#         print("*", end="")
#     print()

# 45. 

# start = int(input("Enter the start number: "))
# end = int(input("Enter the end number: "))

# print("Odd numbers between them:")

# for num in range(start, end + 1):
#     if num % 2 != 0:   # odd number check
#         print(num)

# 46.

# num = int(input("Enter a number: "))

# n = abs(num)   # handle negative numbers
# total = 0

# while n > 0:
#     digit = n % 10      # extract last digit
#     total += digit
#     n //= 10            # remove last digit

# print("Sum of digits:", total)

# 47. 

# num = int(input("Enter a number: "))

# n = num
# rev = 0

# while n > 0:
#     rev = rev * 10 + n % 10  # add last digit
#     n //= 10                  # remove last digit

# if rev == num:
#     print("Palindrome")
# else:
#     print("Not a palindrome")


# 49. 

# n = int(input("Enter a number: "))

# for i in range(n):
#     print("*", end="")

# 50.

# n = int(input("Enter a number: "))

# for i in range(n, 0, -1):
#     print(i)

# print("Blast off!")

# 51.

# n = int(input("Enter a number: "))

# for i in range(1, n + 1):
#     print(f"Row {i}")

# ask the user for n number and print python exactly n times