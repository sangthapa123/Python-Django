# Practice Excercises for Decorators
"""
1. Basic Decorators-Logging
Create a decorator named log_call that prints:
    calling function <function_name>

    before function runs:
    Task:
    Decorate three bfunction: add(a, b), greet(name), and square(n).

"""
# def log_call(function):
#     def wrapper(*args, **kwargs):
#         print(f"Calling function {function.__name__}")
#         return function(*args, **kwargs)
#     return wrapper

# @log_call
# def add(a, b):
#     return a + b

# @log_call
# def greet(name):
#     return f"Hello, {name}!"

# @log_call
# def square(n):
#     return n * n    

# print(add(3, 4))
# print(greet("Alice"))
# print(square(5))

# 2. Decorator that measures execution time
"""
Create a decorator called measure_time that prints how many seconds a function took to execute.

Task:
Decorate a function slow_task() that sleeps for 2 seconds.
"""


# import time
# def measure_time(function):
#     def wrapper(*args, **kwargs):
#         start_time = time.time()
#         result = function(*args, **kwargs)
#         end_time = time.time()
#         print(f"{function.__name__} took {end_time - start_time} seconds to execute.")
#         return result
#     return wrapper

# @measure_time
# def slow_task(seconds):
#     time.sleep(seconds)
#     return "Task completed"

# print(slow_task(2))

#  3. Decorator with Arguments (like role_required)
"""
Write a decorator named repeat(n) that runs the function n times.
Example: 

@repeat(3)
def hello():
print("Hello!")

Output:
Hello!
Hello!
Hello!
"""
# def repeat(n):
#     def decorator(func):
#         def wrapper(*args, **kwargs):
#             for i in range(n):
#                 func(*args, **kwargs)
#         return wrapper
#     return decorator
    
# @repeat(3)
# def hello():
#     print("Hello!")
# hello()

# 4. Create your own cache Decorator

"""
write a decorator memoize that:
 . Stores results in a dictionary
 . prints "fetching from cache" when the result already exists
 . prints "Calculating...." when running the original function

 Task:
 Decorate a function fib(n) that returns the nth fibinocci number.
"""
# def memoize(func):
#     cache = {}
#     def wrapper(n):
#         if n in cache:
#             print("Fetching from cache")
#             return cache[n]
#         else:
#             print("Calculating...")
#             result = func(n)
#             cache[n] = result
#             return result
#     return wrapper

# @memoize
# def fib(n):
#     if n <= 1:
#         return n
#     else:
#         return fib(n-1) + fib(n-2)

# print(fib(6))

# 5. Login_required practice

"""
given: 
logged_in = false

create:
 . profile() -> only logged_in users can see
 . settings() -> only logged in users can access

 Decorate both @login_required.
 Try toggling:
 Logged_in = True

 and test again.
"""
# loggedin = False

# def login_required(func):
#     def wrapper(*arg, **kwargs):
#         if loggedin:
#             func(*arg, **kwargs)
#         else:
#             print("you must log in first")
#     return wrapper
# @login_required
# def profile():
#     print("this is profile page")

# @login_required
# def settings():
#     print("this is settings page")

# profile()
# settings()

# loggedin = True
# profile()
# settings()

# 6. Role required (["admin", "editor"])
"""
Create a system with:
Role = "viewer"

Make functions:
. delete_post()
. edit_post()
. view_status()

Use: 
@role_required(["admin"])
@role_required(["admin", "editor"])
@role_required(["admin", "editor", "viewer"])

Test by changing role values.


"""
# role = "viewer"

# def role_required(roles):
#     def decorator(func):
#         def wrapper(*args, **kwargs):
#             if role in roles:
#                 func(*args, **kwargs)
#             else:
#                 print("you are not authorized to use this page")
#         return wrapper
#     return decorator

# @role_required(["admin"])
# def delete_post():
#     print("delete post")
# @role_required(["admin", "editor"])
# def edit_post():
#     print("edit post")
# @role_required(["admin", "editor", "viewer"])
# def view_status():
#     print("view status")

# delete_post()
# edit_post()
# view_status()  

# 7. Multiple decorators Together

"""
Write two decorators:
1. Uppercase -> Converts output to uppercase
2. Exclaim -> Adds "!!" at the end of the output

Decorate:
@Exclaim
@Uppercase
def greet():
return "good morning"

Expected:
GOOD MORNING!!

Then switch the decorator order and observe the difference.
"""
# def upper(func):
#     def wrapper(*args, **kwargs):
#         return func(*args, **kwargs).upper()
#     return wrapper
# def exclaim(func):
#     def wrapper(*args, **kwargs):
#         return func(*args, **kwargs)+"!!"
#     return wrapper

# @upper
# @exclaim
# def greet(name):
#     return f"Hello, {name}"
# print(greet("John"))

# 8. Decorator that validates input

"""
Write a decorator ensure_positive that checks if all arguments are positive.

example:
@ensure_positive
def divide(a, b):
return a/b

if user calls:
divide(-4, 2)

Output:
All numbers must be positive

"""
# def ensure_positive(func):
#     def wrapper(*args, **kwargs):
#         for arg in args:
#             if arg < 0:
#                 return "All numbers must be positive"
#         return func(*args, **kwargs)
#     return wrapper

# @ensure_positive
# def divide(a, b):
#     return a/b
# print(divide(-4, 2))

# 9. Decorators that counts how many times a function was called

"""
create count_calls decorator.

it should print:

Function <name> has been called <n> times

Task:
Apply it to any two functiions.
"""
def count_calls(func):
    def wrapper(*args, **kwargs):
        wrapper.calls += 3
        return func(*args, **kwargs)
    wrapper.calls = 0
    return wrapper

@count_calls
def add(a, b):
    return a + b

@count_calls
def subtract(a, b):
    return a - b

print(add(2, 3))
print(subtract(2, 3))
print(add.calls)
print(subtract.calls)




