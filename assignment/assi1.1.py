# reminder when divided by 5
# number=int(input("Enter a number: "))
# remainder=number%5
# print("The remainder when divided by 5 is", remainder)  
# =====================================================

# sum of digits of 2 digit number
# number=int(input("Enter a two digit number: "))
# tens=number//10
# units=number%10
# sum_of_digits=tens+units
# print("The sum of the digits is", sum_of_digits)
# =====================================================

# sum of three digits of a number
# number=int(input("Enter a three digit number: "))
# hundreds=number//100
# tens=(number//10)%10  
# units=number%10
# sum_of_digits=hundreds+tens+units
# print("The sum of the digits is", sum_of_digits)
# =====================================================

# reverse of a two digit number
# number=int(input("Enter a two digit number: ")) 
# tens=number//10
# units=number%10
# reverse=units*10+tens
# print("The reverse of the number is", reverse)  
# =====================================================

# average of five numbers
# a=int(input("Enter first number: "))
# b=int(input("Enter second number: "))   
# c=int(input("Enter third number: "))
# d=int(input("Enter fourth number: "))
# e=int(input("Enter fifth number: "))
# average=(a+b+c+d+e)/5
# print("The average of the five numbers is", average)
# ===================================================== 

# sum of numbers 1 to  n
# n=int(input("Enter a number: "))
# sum_n = n*(n+1)//2
# print("The sum of numbers from 1 to", n, "is", sum_n)
# =====================================================

# Factorial of a number
n=int(input("Enter a number: "))  
factorial=1
for i in range(1,n+1):
    factorial=factorial*i 
print("The factorial of", n, "is", factorial)
# =====================================================


# area of parallelogram
base=int(input("Enter base of parallelogram: "))  
height=int(input("Enter height of parallelogram: "))
area=base*height  
print("The area of the parallelogram is", area)
# =====================================================

# perimeter of parallelogram
side1=int(input("Enter base of parallelogram: "))    
side2=int(input("Enter side of parallelogram: "))
perimeter=2*(side1+side2)
print("The perimeter of the parallelogram is", perimeter)
# =====================================================


# area of trapezium
base1=int(input("Enter first base of trapezium: ")) 
base2=int(input("Enter second base of trapezium: "))
height=int(input("Enter height of trapezium: "))
area=0.5*(base1+base2)*height
print("The area of the trapezium is", area)
# =====================================================

# perimeter of trapezium
side1=int(input("Enter first side of trapezium: "))    
side2=int(input("Enter second side of trapezium: "))    
side3=int(input("Enter third side of trapezium: "))
side4=int(input("Enter fourth side of trapezium: "))
perimeter=side1+side2+side3+side4
print("The perimeter of the trapezium is", perimeter) 
# =====================================================

# area of rhombus
d1=int(input("Enter first diagonal of rhombus: " ))
d2=int(input("Enter second diagonal of rhombus: "))  
area=0.5*d1*d2
print("The area of the rhombus is", area)
# =====================================================


# perimeter of rhombus
side=int(input("Enter side length of rhombus: "))
perimeter=4*side
print("The perimeter of the rhombus is", perimeter) 
# ===================================================== 


# triple of a number
a=int(input("Enter a number: "))
result=3*a
print("The triple of the number is", result)
# =====================================================


# quotient and remainder
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
quotient=a//b
remainder=a%b
print("The quotient is", quotient)
print("The remainder is", remainder)    
# =====================================================


# sum of squares of two numbers
a=int(input("Enter first number : "))
b=int(input("Enter second number : "))
sum=(a**2)+(b**2)
print("The sum of squares is", sum) 
# =====================================================


# sum of cubes of two numbers
x=int(input("Enter first number: "))
y=int(input("Enter second number: "))
sum=(x**3)+(y**3)
print("The sum of cubes is", sum)  
# =====================================================

# evaluate (a+b)*c
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
c=int(input("Enter third number: "))
result=(a+b)*c
print("The result of (a+b)*c is", result)
# =====================================================


# evaluate (a+b)/c
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
c=int(input("Enter third number: "))
result=(a-b)/c
print("The result of (a-b)/c is", result)
# =====================================================


# convert minutes to seconds
minutes=int(input("Enter time in minutes: "))
seconds=minutes*60
print("The time in seconds is", seconds)
# =====================================================


# convert hours to minutes
hours=int(input("Enter time in hours: "))
minutes=hours*60
print("The time in minutes is", minutes)
# =====================================================


# convert days to hours
days=int(input("Enter time in days: "))
hours=days*24
print("The time in hours is", hours)
# =====================================================



# convert weeks to days
week=int(input("Enter time in weeks: "))
days=week*7
print("The time in days is", days)
# =====================================================


# perimeter of hexagon
side=int(input("Enter side of hexagon : "))
perimeter=6*side
print("The perimeter of the hexagon is", perimeter)
# =====================================================


# area of hexagon
side=int(input("Enter side of hexagon : "))
area=(3*(3**0.5)*side**2)/2
print("The area of the hexagon is", area)
# =====================================================


# total price including tax    
price=int(input("Enter price of item: "))
tax=int(input("Enter tax percentage: "))
total=price +(price*tax/100)
print("The total price including tax is", total)
# =====================================================
