# class A:
#     def show(self):
#         print("this is class A")


# # B is subclass of superclass A
# class B(A):
#     # method overriding
#     def show(self):
#         super().show()
#         print("This is class B")


# # a = A()
# # a.show()

# b = B()

# b.show()


#
# class User:  # Base user class
#     def __init__(self, username, password):
#         self.username = username

#         if len(password) < 6:
#             raise Exception("Password must be at least 6 chars long")

#         self.password = password

#     def show_info(self):
#         print(
#             f"""

#             Username : {self.username}
#             Password : {self.password}

#               """
#         )


# class Student(User):
#     def __init__(self, username, password, classname):
#         super().__init__(username, password)
#         self.classname = classname

#     def show_info(self):
#         super().show_info()
#         print(f" Class of admission =  {self.classname} ")


# class Teacher(User):
#     def __init__(self, username, password, salary):
#         super().__init__(username, password)
#         self.salary = salary

#     def show_info(self):
#         super().show_info()
#         print(f" Salary =  Rs. {self.salary} ")


# ram = User("Ram", "ram@123")

# ram.show_info()

# s1 = Student("shyam", "shyam@123", "class 10")
# s1.show_info()

# t1 = Teacher("hari", "hari@123", 30000)
# t1.show_info()

# User -> General
# User -> inherit -> Student -> Specialization


#
# class A:
#     pass
#     # def show(self):
#     #     print("class A")


# class B:
#     pass
# def show(self):
#     print("class B")


# class C(A, B):
#     # a-> show
#     # b-> show
#     pass
#     # def show(self):
#     #     print("class C")


# c = C()
# c.show()

# MRO -> Method Resolution Order
# print(C.__mro__)
# C, A, B, obj -> no attribute
# Vehicle -> Bike -> Sports??

# C (B)


# Special methods, magic methods, dunder methods
# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def __add__(self, other):
#         # new_point = Point(self.x + other.x, self.y + other.y)
#         # return new_point
#         return Point(self.x + other.x, self.y + other.y)

#     # def __sub__(self, other):
#     #     pass
#     #     # implement yourself
#     def __sub__(self, other):
#         nx = self.x - other.x
#         ny = self.y - other.y
#         d = (nx**2 + ny**2) ** 0.5
#         return d

#     def __str__(self):
#         return f"P({self.x}, {self.y})"


# p1 = Point(1, 1)
# p2 = Point(5, 5)
# p3 = Point(4, 6)
# print(5) => "5"
# print([1, 2, 4]) => "[1, 2, 4]"
# print(p1)
# print(p2)
# 5 + 5 = 10
# "a" + "b" = "ab"
# [1, 2] + [2, 3] = [ 1, 2, 2, 3]
# p3 = p1 + p2

# print(p3)
# print(p1 - p2, " units")
