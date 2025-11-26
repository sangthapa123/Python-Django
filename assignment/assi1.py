
# add two numbers
# input two numbers
# use + operator to add them
# print the sum 
# a=int(input("Enter first number: "))
# b=int(input("Enter second number: "))
# sum=a+b
# print("the sum is", sum)
# =====================================================


# subtract two numbers
# input two numbers
# use - operator to subtract them
# print the subtraction
# a=int(input("Enter first number: "))
# b=int(input("Enter second number: "))
# sub=a-b
# print("the subtraction is", sub)  
# =====================================================


# multiply two numbers
# input two numbers 
# use * operator to multiply them
# print the multiplication
# a=int(input("Enter first number: "))
# b=int(input("Enter second number: "))
# mul=a*b
# print("the multiplication is", mul)
# =====================================================


# divide two numbers
# input two numbers
# use / operator to divide them
# print the division
# a=int(input("Enter first number: "))
# b=int(input("Enter second number: "))
# div=a/b
# print("the division is", div)
# =====================================================


# modulus of two numbers
# input two numbers
# use % operator to find modulus
# print the modulus
# a=int(input("Enter first number: "))
# b=int(input("Enter second number: "))
# mod=a%b
# print("the modulus is", mod)
# =====================================================


# exponentiation of two numbers
# input two numbers
# use ** operator to find exponentiation
# print the exponentiation
# a=int(input("Enter first number: "))
# b=int(input("Enter second number: "))
# exp=a**b
# print("the exponentiation is", exp)
# =====================================================

# square of a number
# input a number    
# use ** operator to find square root     
# print the square root
# a=int(input("Enter a number: "))
# sqr=a**2
# print("the square  is", sqr)
# =====================================================

# cube of a number
# input a number
# use ** operator to find cube root     
# print the cube root
# a=int(input("Enter a number: "))
# cube=a**3
# print("the cube root is", cube)
# =====================================================


# floor division of two numbers
# input two numbers
# use // operator to find floor division
# print the floor division
# a=int(input("Enter first number: "))
# b=int(input("Enter second number: "))
# floordiv=a//b
# print("the floor division is", floordiv)
# =====================================================

# sum of three numbers
# input three numbers   
# use + operator to add them
# print the sum
# a=int(input("Enter first number: "))
# b=int(input("Enter second number: "))
# c=int(input("Enter third number: "))
# sum=a+b+c
# print("the sum is", sum)
# =====================================================


# average of three numbers
# input three numbers
# use + operator to add them and divide by 3
# print the average
# a=int(input("Enter first number: "))
# b=int(input("Enter second number: "))
# c=int(input("Enter third number: "))
# avg=(a+b+c)/3
# print("the average is", avg)
# =====================================================

# area of rectangle
# input length and breadth
# use * operator to find area
# print the area
# length=int(input("Enter length of rectangle: "))
# breadth=int(input("Enter breadth of rectangle: "))
# area=length*breadth
# print("the area of rectangle is", area)
# # =====================================================


length=int(input("Enter length of rectangle: "))
breadth=int(input("Enter breadth of rectangle: "))
perimeter=2*(length+breadth)
print("The perimeter of the rectangle is", perimeter)
# =====================================================

# area of square
# input side
# use ** operator to find area
# print the area
side=int(input("Enter side of square: "))
area=side**2
print("The area of the square is", area)
# =====================================================

# perimeter of square
# input side
side=int(input("Enter side of square: "))
perimeter=4*side
print("The perimeter of the square is", perimeter)
# =====================================================

# area of circle
# input radius
# import math
radius=float(input("Enter radius of circle: "))
# area=math.pi*radius**2
area=3.14*radius**2
print("The area of the circle is", area)
# =====================================================

# circumference of circle
# input radius
radius=float(input("Enter radius of circle: "))
# import math   
# circumference=2*math.pi*radius
circumference=2*3.14*radius
print("The circumference of the circle is", circumference)  
# =====================================================

# celcius to fahrenheit
# input celcius 
celcius=float(input("Enter temperature in celcius: "))
fahrenheit=(celcius*9/5)+32
print("The temperature in fahrenheit is", fahrenheit)   
# =====================================================

# fahrenheit to celcius
# input fahrenheit
fahrenheit=float(input("Enter temperature in fahrenheit: "))
celcius=(fahrenheit-32)*5/9
print("The temperature in celcius is", celcius)
# =====================================================

# simple interest
# input principal, rate and time
principal=float(input("Enter principal amount: "))
rate=float(input("Enter rate of interest: "))
time=float(input("Enter time in years: "))
simple_interest=(principal*rate*time)/100
print("The simple interest is", simple_interest)
# =====================================================

# compound interest
# input principal, rate and time
principal=float(input("Enter principal amount: "))
rate=float(input("Enter rate of interest: "))
time=float(input("Enter time in years: "))
compound_interest=principal*(1+rate/100)**time - principal
print("The compound interest is", compound_interest)    
# =====================================================


# swap two numbers
# input two numbers
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
a, b = b, a
print("After swapping, first number is", a)
print("After swapping, second number is", b)
# =====================================================

# area of triangle
# input base and height
base=int(input("Enter base of triangle: "))
height=int(input("Enter height of triangle: "))
area=0.5*base*height
print("The area of the triangle is", area)  
# =====================================================

# perimeter of triangle
# input three sides
side1=int(input("Enter first side of triangle: "))
side2=int(input("Enter second side of triangle: "))
side3=int(input("Enter third side of triangle: "))
perimeter=side1+side2+side3
print("The perimeter of the triangle is", perimeter)
# =====================================================

# sqare root of a number
# input a number
number=float(input("Enter a number: "))
square_root=number**0.5
print("The square root of the number is", square_root)  
# =====================================================

