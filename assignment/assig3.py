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
# temp = float(input("Enter the temperature in celsius:"+"°C"+" "))
# if temp > 30:
#     print("It's hot outside.")
# else:
#     print("It's cold outside.")

temp_input = input("Enter the temperature (e.g., 30°C): ")

# Remove °, C, c, and spaces so only the number remains
temp_clean = temp_input.replace("°", "").replace("C", "").replace("c", "").strip()

temp = float(temp_clean)

if temp > 30:
    print("It's hot outside.")
else:
    print("It's cold outside.")
