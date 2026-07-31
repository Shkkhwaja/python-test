# class Car:
#     age=12 #attribut

#     def pr():
#         print("The method")  #method


# print(Car.age)
# Car.pr()


# class Stu:
#     fees = 152.22

#     def name(self):
#         print("hussain")

# stu1 = Stu()
# stu2 = Stu()
# print(stu1.fees)
# print(stu2.fees)

# stu1.name()




# class Bag:
#     def __init__(self,material,zip):
#         self.material = material
#         self.zip = zip
        

# bag = Bag("cotton",2)



# class Animal:
#     a=25
#     def __init__(self,name):
#         self.name = name    #instance/object attribute
    
#     def details(self):      #instance/object method
#         print(f"how are you {self.name}")

#     @classmethod   #decorator
#     def det(cls):
#         print(f"class decorator {cls.a}")

#     @staticmethod
#     def stamet():
#         print("this is an static method")

# obj = Animal("lion")

# print(obj.name)

# obj.det()        
# obj.stamet()        



#inheritance

# class Animal:
#     a=22
#     def __init__(self,name):
#         self.name = name

#     def details(self):
#         print(f"My name is {self.name}")

# class Human(Animal):
#     pass


# obj1 = Animal("hussain")

# obj2 = Human("shaikh")

# obj1.details()
# obj2.details()
# print(obj2.a)

#A inheritance means the child class has all the power of parent class measn it has access for attribute, methods and initiate.


#multilevel inheritance

# class BagFactory:
#     def __init__(self,material,zip,pockets):
#         self.material = material
#         self.zip = zip
#         self.pockets = pockets
        

#     def details(self):
#         print(f"the bag material is : {self.material}")
#         print(f"the bag ZIP is : {self.zip}")
#         print(f"the bag pockets is : {self.pockets}")



# bag1 = BagFactory("cotton",3,5)
# bag1.details()


# class Reebok(BagFactory):
#     def __init__(self, material, zip, pockets,colour):
#         super().__init__(material, zip, pockets)
#         self.colour = colour
        
#     def col(self):
#         print(f"this is the colour {self.colour}")

# bag2 = Reebok("Polister",2,4,"gray")
# bag2.details()
# bag2.col()

# class Campus(Reebok):
#     def __init__(self, material, zip, pockets, colour):
#         super().__init__(material, zip, pockets, colour)

#     def data(self):
#         print(f"campus {self.colour}")

# cam = Campus("new cotton",5,5,"green")

# cam.data()



#multiple inheritance

class Animal:
    def __init__(self,name):
        self.name=name

class Human:
    def __init__(self,id):
        self.id = id

class Robot(Animal,Human):
    def __init__(self, name,id):
        Animal.__init__(self,name)
        Human.__init__(self,id)

rob = Robot("new hus",122)

print(rob.id)
print(rob.name)




























