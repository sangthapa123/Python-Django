# Real-Life + Fun Simulation Problems
"""
All problems focus on:
.Function behaviour
. Print vs return
. None checking
. if/else flow
. Logic building

"""
# 1. Candy Machine simulator
"""
 A shop sells one candy for 10 rupees.
 write function buy_candy(money) that:
 . if the student gives 10 or more rupees ->return "candy bought"
 . if the money is less than 10 -> print "not enough money"

 After calling the function:
 . if the function returned something, print : "customer got the candy"
 . if nothing returned print, "No candy given"

"""
# def buy_candy(money):
#     if  money >= 10:
#         print("candy bought")
#         return True
#     else:
#         print("not enough money")
#         return None
    
# result = buy_candy(6)
# if result:
#         print("customer got the candy")
# else:
#         print("No candy given")


# 2. pubg/freefire health booster
"""
A player's health is from 0 to 100.
create a function heal(health):
. print ("Healing ...") every time the function is runs
. if the health is 100 or more -> return nothing(return none)
. else -> return "healed"

after calling function
. if values was returned -> print "Healing Successful"
. if it returned none -> print "player already full health"

"""
# def heal(health):
#     print("healing...")
#     if health >= 100:
#         return None
#     else:
#         return "healed"
    
# result = heal(120)
# if result:
#     print("Healing Successful")
# else:
#     print("player already full health")


# 3. ATM withdrawal Machine
"""
write a function withdraw(balance,amount):
. if amount is greater than balance -> print "insufficient balance"
. else -> return return the new balance(balance-amount)

after calling function
. if values was returned -> print "New balance: <value>"
. if it didnt return a value print "Transaction failed"

"""
# def withdraw(balance, amount):
#     if amount > balance:
#         print("insufficient balance")
#     else:
#         new_balance = balance - amount
#         return new_balance

# result = withdraw(1000, 500)
# if result:
#     print(f"New balance: {result}")
# else:
#     print("Transaction failed")

# 4. School Attendance system
"""
Create a function mark_attendance(name,present):
.if present is true -> return "Marked present"
.if present is false -> return "Student is absent"

After calling the function
. if return value exists -> print "Attendance saved"
. else -> print "Attendance not saved"
"""

    
"""
BIG CONFUSION
"""
# def mark_attendance(name, present):
#     if present is True:
#         return "Marked present"
#     elif present is False:
#         return "Student is absent"


# # Calling the function
# result = mark_attendance("Alice", True)   

# if result:
#     print("Attendance saved")
# else:
#     print("Attendance not saved")

# 5. Mobile Battery Checker

"""
Create a function battery_status(level):
. if battery level is less than 20 -> print "Low battery"
. otherwise -> return "Battery ok"

After calling:
. print "phone is functionning normally" if return value exists
. otherwise print-> "Phone battery Warning"


"""
# def battery_status(level):
#     if level < 20:
#         print("low battery")
#         return None
#     else:
#         return "battery ok"
    
# result = battery_status(100)
# if result:
#     print("phone is functionning normally")
# else:
#     print("Phone battery Warning")

# 6. Restaurant Billing System 

"""
Create a function calculate_bill(items):
(here, items is a list of items prices, for example [100,50,130])
 
The function should:
. if the list is empty -> print "No items selected"
. otherwise -> return the total bill

After calling :
. if value returned -> print  "Total bill is :<value>"
. else -> print "Cannot generate bill"
"""

# def calculate_bill(items):
#     if len(items) == 0:      # or: if not items
#         print("No items selected")
#         return None
#     else:
#         return sum(items)


# # Calling the function
# result = calculate_bill([])  

# if result:
#     print("Total bill is:", result)
# else:
#     print("Cannot generate bill")
#


# 7. Weather Alert system 

""""
create a function check_temp(temp):
. if temp is more than 40 -> print "too hot! stay hydrated"
. if temp is less than 0 -> print "too cold! stay warm"
. otherwise -> return "Weather is fine"

"""

# def check_temp(temp):
#     if temp > 40:
#         print("too hot! stay hydrated")
#     elif temp < 0:
#         print("too cold! stay warm")
#     else:
#         return "Weather is fine"

# # Calling the function
# result = check_temp(100)  
# print(result)

# 8. Game XP reward System

"""
create a function reward(xp)
. if xp is greater than 1000 -> return "Level up"
. otherwise -> print "Earn more xp to level up"

after calling:
. if return value exists -> print "Congratulations!"
. else -> return "Try again"

"""
# def reward(xp):
#     if xp > 1000:
#         return "Level up"
#     else:
#         print("Earn more xp to level up")
#         return None

# result = reward(5000)

# if result:
#     print("Congratulations!")
# else:
#     print("Try again")

# print(result)

# 9. Delivery service simulator

"""
A company only delivers within 50km.

write function delivery_status(distance):

.if distance > 50 -> print "Delivery not available 
. else -> return "Delivery on the way"

after calling :
. if return value exists -> print "Order placed Successfully"
. else -> print "Order failed"

"""
# def delivery_status(distance):
#     if distance > 50:
#         print("Delivery not available")
#     else:
#         return "Delivery on the way"
    
# result = delivery_status(34)
# if result:
#     print("Order placed Successfully")
# else:
#     print("Order failed")

# 10. Traffic ligh system

"""
create a function traffic(color)

.if color is "red" -> print "Stop"
.if color is "yellow" -> print "Slow down"
.if color is "green" -> return "Go"

after calling:
. if return value exists -> print "Drive"
. else -> print "wait"

"""
# def traffic(color):
#     if color == "red":
#         print("Stop")

#     elif color == "yellow":
#         print("Get ready")

#     else:
#         return "Go"
    
# result = traffic("green")
# if result:
#     print("Drive")
# else:
#     print("Wait")


# 11. Youtube video loader

""""
Create a function load_video(speed):

. if speed <2 mbps -> print "Buffering"
. else return "playing video"

after calling:
. if return -> print "Enjoy your video"
. else -> print "internet slow, please wait"

"""

# def load_video(speed):
#     if speed < 2:
#         print("buffering")
#     else:
#         print("playing video")

# result = load_video(1)
# if result:
#     print("Enjoy your video")
# else:
#     print("Internet slow, Please wait")