##########.........REST OF THE ASSIGNMENTS FROM ASSIGNMENT 5........##############

# 12. Grocery Checkout

"""
create a function checkout(amount)
. if amount is 0 print -> "your cart is empty"
. else -> return "payment successfull"

after call :
. if returned -> print "Thank you nfor shopping"
. else print "Could not checkout"

"""
# def checkout(amount):
#     if amount == 0:
#         print("Your cart is empty")
#     else:
#         return "Payment successfull"
    
# result = checkout(0)
# if result:
#     print("Thank you for shopping")
# else:
#     print("Can not checkout")

# 13. Password strength Checker:
"""
create a function check_password(password)
. if password length is less than 8 -> print"Weak Password"
. else return "Strong password"

after call"

. "secure" if returned value exits.
. "Please choose strong password"

"""
# def check_password(password):
#     if len(password)<8:
#         print("Weak Password")
#     else:
#         return "Strong password"

# result = check_password("sangi")
# if result:
#     print("Secure")
# else:
    # print("Please choose Stronger password")


# 14. Bus booking system

"""
create a function book_ticket(seats)
. if seats == 0 ->print "Sold out"
. else return "Ticket booked"

after calling, check if the function returned something.

"""

# def book_ticket(seats):
#     if seats == 0:
#         print("Sold out")
#     else:
#         return "Ticket booked"
    
# result = book_ticket(0)
# print(result)

# 15. Nepali mobile Recharge Simulator
"""
create a function recharge(amount)
. if amount < 10 -> "Minimum recharge is 10"
. else return "Rescharge successfull"

after calling
. if returned -> print "balance updated"
. else -> print "Recharge failed"

"""
# def recharge(amount):
#     if amount < 10:
#         print("Minimum recharge is 10")
#     else:
#         return "Recharge Successful"
# result = recharge(10)
# if result:
#     print("balanced updated")
# else:
#     print("Recharge failed")

# 16. Water bottle level Checker
"""
create a function check_water(level)
. if level ==0 -> print "bottle empty"
. if level <50 -> print "need refill soon"
. if level >= 50 -> print "water level ok"

after calling:

use return checking.

"""
def check_water(level):
    if level == 0:
        print("Bottle empty")
    elif level < 50:
        print("Need refill soon")
    else:
        return "Water level ok"
result = check_water(49)
print(result)