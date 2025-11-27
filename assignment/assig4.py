# List- Practical USage Questions

# 1. Add item
# Create a list called cities = ["Pokhara", "Lalitpur", "heatauda"]. Ask the user for a new city name and add it to the list. Finally, print the updated list.
# Hint : Use cities.append(new_city)

# cities = ["Pokhara", "Lalitpur", "Hetauda"]
# cities.append("Butwal")
# print(cities)

# 2. Remove item
# ask the user to enter a city to remove from the same list. remove it, otherwise show "City not found"
# hint:check with if city in cities:before removing.

# cities = ["Butwal", "Bhairahawa", "Chitwan", "Kawasoti"]
# city = input("Enter city you want to delete :")
# if city in cities:
#     cities.remove(city)
#     print("deleted")
# else:
#     print("City not found")
# print(cities)

# 3. Modify item
# Change the city at index 2 to uppercase.
# Hint: index assignment ->cities[2].upper

# cities = ["butwal", "bhairahawa", "chitwan", "kawasoti"]
# cities[1] = cities[1].upper()
# print(cities)

# For all cities Uppercase

# cities = ["New York", "London", "Paris", "Tokyo", "Sydney"]

# # Convert all cities to uppercase
# cities = [city.upper() for city in cities]

# print(cities)

# insert item at specific index
# insert "janakpur" at index 1 in the cities list.
# Hint : use insert(1, "janakpur")

# cities = ["butwal", "chitwan", "kawasoti", "kathmandu"]
# cities.insert(1,"janakpur")
# print(cities)

# 5. Create a list of roll numbers and print squares
# ask the user to continuously enter the roll numbers until they enter -1. store them in a list rolls. then print each roll number and its square. 
# example output: 7->49, 3->9 etc.
# # hint: while loop to collect numbers, then  a for looop.

# while True:
#     roll_no = int(input("Enter roll number,(hint:-1 is for stopping the number "))
#     if roll_no == -1:
#             break
#     print(f"{roll_no}->{roll_no**2}" )

# Tuple- Pratical usage questions
# 6. show immutability
# create a tuple fruits =("apple","orange","mango","banana") try to change banana to BANANA and observe what happens. 
# Hint : Tuples can not modified

# fruits =("apple","orange","mango","banana")
# fruits[3]=fruits.upper[3]
# print(fruits)

# AttributeError: 'tuple' object has no attribute 'upper'
 

# 7. convert->modify->convert back
# Convert the tuples into a list, add "orange", and convert it back to the tuple named fruits_final.
# Hint : temp = list(fruits)-> modify->fruits_final = tuple(temp)


# fruits = ("apple", "banana", "grapes")# Original tuple
# temp = list(fruits)# Convert tuple to list
# temp.append("orange")# Add "orange" to the list
# fruits_final = tuple(temp)# Convert the list back to tuple
# print(fruits_final)

# 8.indexing tuple
# create marks = (78, 82, 91) print only the highest mark using indexing.
# Hint : Highest is at index 2 if the tuple is sorted.

# marks = (78,82,91) #create marks
# print(marks[2]) #print highest marks


# SET- Practical usage Questions
# 9. Remove duplicates
# craete a list: animala = ["cat", "dog", "cow", "goat"] convert it into a set and print the unique animals. 
# Hint: Use set (animal)

# animal = {"cat", "dog", "cow", "goat","cat"}
# set= set(animal)
# print(set)


# 10. set operations
# given : team_a = {2,5,7,8} team_b = {1,2,3,4}
# a. find players common in  both team
# b. players only in team_a
# c. players only in team_b
# d. players who are exactly in one team

# a.find players common in  both team

# team_a = {2, 4, 6,8}
# team_b ={1, 2, 3, 4}
# common = set(team_a).intersection (set(team_b))
# print(common)

# b. players only in team_a

# team_a = {2, 4, 6,8}
# team_b ={1, 2, 3, 4}
# onlyA = set(team_a)-(set(team_b))
# print(onlyA)

# c.  players only in team_b
# team_a = {2, 4, 6,8}
# team_b ={1, 2, 3, 4}
# onlyB = set(team_b)- (set(team_a))
# print(onlyB)

# d.players who are exactly in one team

# team_a = {2, 4, 6,8}
# team_b ={1, 2, 3, 4}
# oneset = set(team_b)^ (set(team_a))
# print(oneset)

#  11. intersection from lists
# Given: coding = ["alice", "bob", "dilip"] robotics = ["dilip", "suman", "alice"] find the students who joined both clubs. Hint: convert list to sets -->intersection

# coding = ["alice", "bob", "dilip"]
# robotics = ["dilip", "suman", "alice"]
# common = set(coding).intersection(set(robotics))
# print(common)


# 12. Basic set operations
"""create a set: scores = {10,20,30} add 40. remove 10. print final set.
Hint : scores.add(40) and scores.remove(10)"""

# scores ={10,20,30}
# scores.add(40)
# scores.remove(10)
# print(scores)


# 4. DICTIONARY - practical usage questions
# 13. Nested dictionary
"""create a dictionary called book with keys :
"tittle" -> "python Basics"
"author" -> "jhon doe"
"details" -> another dictionary containing:
        "pages" =>250
        "publisher" => "TechPress"
print only the publisher name.
Hint: book["details"]["publisher"]
"""

# book ={
#     "title" : "python basics",
#     "author" : "jhon doe",
#     "details" : 
#     {
#         "pages" : "250",
#         "publisher" : "TechPress"
#     }
        
# }
# print(book["details"]["publisher"])


# 14. Modify value
"""change the "author" value to "jan smith".
Hint : direct reassignment book["author"] = "jan smith" """

# book ={
#     "title" : "python basics",
#     "author" : "jhon doe",
#     "details" :{
#         "pages" : "250",
#         "publisher" : "TechPress"

#     }

# }
# book["author"]  = "jan smith"
# print(book)


# 15. Add new key
"""add a "year" key with value 2024 to the book dictionary.
Hint : book["year"] = 2024"""


# book = {
#     "title" : "python basics",
#     "author" : "jhon smith",
#     "details" :{
#         "pages" : "250",
#         "publisher" : "TechPress"

#     }
# }
# book["year"]= "2024"
# print(book)


#  16. Access deep nested values
""" 
create :
car = {
    "brand" : "toyota",
    "speces" : {
        "engine" : {
            "hp" : 150,
            "type" : "petrol"
            },
        "wheels" : 4
        }
    }
    print only the horsepower(hp) value.
    Hint : car["speces"]["engine"]["hp]
    
"""

# car = {
#     "brand" : "toyota",
#     "speces" : {
#         "engine" : {
#             "hp" : 150,
#             "type" : "petrol"
#             },
#         "wheels" : 4
#         }
#     }

# print(car["speces"]["engine"]["hp"])


# 17. Loop through dictionary
""" 
loop through all keys and values of the car dictionary and print them. 
Hint: for key , value in car.items():
"""

# car = {
#     "brand" : "toyota",
#     "speces" : {
#         "engine" : {
#             "hp" : 150,
#             "type" : "petrol"
#             },
#         "wheels" : 4
#         }
#     }

# for key, value in car.items():
#     print(key, value)

# 18. check existence

"""
check if "brands" exists in the car dictionary, and check if "Tesla" exists as a value in the "brands" key.
Hint : use in car.keys() and car.values()
"""

# car = {
#     "brands": ["Toyota", "BMW", "Audi", "Mercedes"]
# }
# # Ask user for a brand name
# brand_to_check = input("Enter a brand name: ")

# # Check if it exists in the list
# if "brands" in car and brand_to_check in car["brands"]:
#     print(f"{brand_to_check} exists in the list.")
# else:
#     print(f"{brand_to_check} does NOT exist in the list.")


#  BONUS QUESTION - Combination of all topics
# 19. Student management system(mini-program)
""""
create a dictionary called data where key is a student id (eg. 101,102,103...) and the value is a list of hobbies they have.
Eg. (do Not use this exact one)
data ={
    101 : ["reading", "cycling"],
    102 : ["gaming"],
    103 : ["swimming", "cycling"],
    
    }
    tasks:
    1. print all unique hobbies done by students(use sets)
    2. print ids of students who have more than 1 hobby
    3. print ids of students who have "cycling" as one of their hobbies

    Hints: Convert all the hobby lists into a set using union(set1 | set2)
    check length of each hobby list.
    use "cycling" in hobby_list.

"""

# data = {
#     101 : ["reading", "cycling"],
#     102 : ["gaming", "cycling"],
#     103 : ["swimming", "cycling"],  
# }


#  1. print all unique hobbies done by tudents(use sets)
# unique_hobbies = set()
# for hobby_list in data.values():
#     unique_hobbies |= set(hobby_list)
# print("Unique hobbies:", unique_hobbies)

#  2. print ids of students who have more than 1 hobby
# more_than_one_hobby = []
# for hobby_list in data.values():
#     if len(hobby_list) > 1:
#         more_than_one_hobby.append(hobby_list) 
#         # or more_than_one_hobby.append(hobby_list[0])
#         # more_than_one_hobby.append(hobby_list[1])
#         # more_than_one_hobby.append(hobby_list[2])
# print("Students with more than one hobby:", more_than_one_hobby)

#  3.
# cycling =[]
# for hobby_list in data.values():
#     if "cycling" in hobby_list:
#         cycling.append(hobby_list)
# print("Students who have 'cycling' as one of their hobbies:", cycling)

# 20.you are given a list of students and the subjects they have taken. create the following dictionary(you may add your own sample values):

"""
enroll = {

    "arjun" : ["math", "english","science"],
    "bishal" : ["nepali"],
    "chadani" : ["math", "computer"],
    "deepa" : ["science", "math"],
    "ekta" : ["computer", "english"],
    
    }
    Tasks:
    1. print the names of students who study both math and science.
    2. create a set of all subjects are taking (no duplication)
    3. create a tuple containing only the students who take exactly 1 subject.
    4. remove "english" from ekta's subject list and print the updated list.

    Hints:
    1. Check "math" in enroll[name] and "science" in enroll[name]
    2. convert each list to the set and then union all sets to get unique subjects.
    3. stire name in list ->convert to tuple() at the end
    4. use .remove("english") on the list inside the dictionary

"""

enroll = {

    "arjun" : ["math", "english","science"],
    "bishal" : ["nepali"],
    "chadani" : ["math", "computer"],
    "deepa" : ["science", "math"],
    "ekta" : ["computer", "english"],
}

# 1. Check "math" in enroll[name] and "science" in enroll[name]

# students =[]

# for name, subjects in enroll.items():
#     if "math" in subjects and "science" in subjects:
#         students.append(name)

# print(" and ".join(students), "study both math and science.")

# # 2. create a set of all subjects are taking (no duplication)

# subjects = set()
# for students in enroll.values():
#     subjects |= set(students)
# print("unique subjets:", subjects)

# # 3. create a tuple containing only the students who take exactly 1 subject.
# single_subjects =[]

# for name, subjects in enroll.items():
#     if len(subjects)==1:
#         single_subjects.append(name)
# print("Students who take exactly 1 subject:", tuple(single_subjects))


# # 4. remove "english" from ekta's subject list and print the updated list.

# enroll["ekta"].remove("english")
# print(enroll["ekta"])


# 21. Store inventory system
"""
create a dictionary named store where each key is the item name, and value is another dictionary containing:

    "price" (integer),
    "stock" (available quantity),
Example format (use different items):

store = {
    "soap" : {
        "price" : 50,
        "stock" : 25
        },
    "shampoo" : {
        "price" : 100,
        "stock" : 10
        },
    "brush" : {
        "price" : 30,
        "stock" : 40
        }
    }

Tasks:
1. Add a new product "Toothpaste" with the following details:
    "price" : 60,
    "stock" : 20
2. Reduce the stock of "soap" by 5(simulate purchase)
3. create a list of items that are low stock (stock < 15)
4. print the price of "Shampoo"

Hints:
1. use store["toothpaste"] = {"price" : 60, "stock" : 20}
2. store["soap"]["stock"] -= 5
3. low_stock = []
for item, details in store.items():
    if details["stock"] < 15:
        low_stock.append(item)
4. print(store["shampoo"]["price"])

"""
# Add a new product "Toothpaste" with the following details:
    # "price" : 60,
    # "stock" : 20
# store = {
#     "soap" : {
#         "price" : 50,
#         "stock" : 25
#         },
#     "shampoo" : {
#         "price" : 100,
#         "stock" : 10
#         },
#     "brush" : {
#         "price" : 30,
#         "stock" : 40
#         }

# }

# store["toothpaste"] = {
#             "price" : 60, 
#             "stock" : 20
#             }
            
# # print(store)
# # Reduce the stock of "soap" by 5(simulate purchase)
# store["soap"]["stock"] -= 5
# print(store)

# # create a list of items that are low stock (stock < 15)
# low_stock = []
# for item, details in store.items():
#     if details["stock"] < 15:
#         low_stock.append(item)
# print(low_stock)

# # print the price of "Shampoo"
# print(store["shampoo"]["price"])    
