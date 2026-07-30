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



class Animal:
    a=25
    def __init__(self,name):
        self.name = name    #instance/object attribute
    
    def details(self):      #instance/object method
        print(f"how are you {self.name}")

    @classmethod   #decorator
    def det(cls):
        print(f"class decorator {cls.a}")

    @staticmethod
    def stamet():
        print("this is an static method")

obj = Animal("lion")

print(obj.name)

obj.det()        
obj.stamet()        























