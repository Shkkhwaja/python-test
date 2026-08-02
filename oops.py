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




#polymorphism

# class Animal:
#     def speak():
#         print("Animals can't speak")

# class Human:
#     def speak():
#         print("Human can speak")

# obj = Animal
# obj2 = Human

# obj.speak()
# obj2.speak()


#method overriding (we need inheritance)

# class Animal:
#     a=12
#     def __init__(self,name) -> None:
#         self.name = name

#     def info(self):
#         print(f"this is the animal class my name is {self.name}")


# class Human(Animal):
#     b=12
    
#     def info(self):
#         super().info()
#         print(f"This is the human class my name is {self.name}")

# obj = Human("afroz")

# obj.info()


# when we are doing inheritance and parent and child class have same name
# method name so the child class method will override your parent class method


#practical on inheritance

# class Vehical:

#     def __init__(self,brand):
#         self.brand = brand

#     def start(self):
#         print("Vehical started")


# class Car(Vehical):
#     def __init__(self, brand,model):
#         super().__init__(brand)
#         self.model = model

#     def details(self):
#         print(f"The brand is {self.brand} and the model is {self.model}")


# car = Car("Honda","2025")

# car.start()
# car.details()



# class Person:
#     def __init__(self):
#         pass

#     def introduce(self):
#         print("I am a person.")

# class Student(Person):
#     def introduce(self):
#         # super().introduce()
#         print("I am a student.")

# ne = Student()

# ne.introduce()
