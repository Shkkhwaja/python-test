# fruits = ["Apple","banana","mango","Orange"]

# print(fruits)

# n = [12,13,14,15,16]

# print(n[0])
# print(n[-1])
# print(n[2])


# n1=int(input("enter number"))
# n2=int(input("enter number"))
# n3=int(input("enter number"))
# n4=int(input("enter number"))
# n5=int(input("enter number"))


# n =[n1,n2,n3,n4,n5]

# max=0

# for i in n:
#     sum = sum + i


# n=[]

# for i in range(5):
#     num = int(input(f"Enter number{i + 1} : "))
#     n.append(num)

# largest = n[0]

# for num in n:
#     if num > largest:
#         largest = num

# print("largest number",largest)



# n=[1, 2, 3, 4, 6]

# odd = 0
# even=0


# for i in range(0,len(n)):
#     if n[i] % 2 == 0:
#       even +=1  
#     else:
#        odd +=1

# print("Odd number ",odd)
# print("even number ",even)



# n=[]

# for i in range(5):
#     num = int(input(f"Enter number {i +1} : "))
#     n.append(num)

# for j in range(len(n) -1,-1,-1):
#     print(n[j],end=" ")



# n=[1, 2, 3, 4, 5, 6]

# odd=[]

# for i in range(0,len(n)):
#     if n[i] % 2 == 1:
#         odd.append(n[i])
        

# print(odd)




# n=[10,20,50,40,60]

# n.append(70)
# n.extend([80,90])
# n.insert(0,20)
# n.remove(20)

# n.pop()
# n.pop(2)
# i = n.index(20)

# n.count(20)

# n.sort()
# n.reverse()

# c= n.copy()
# c.pop()
# print(n)
# print(i)
# print("c",c)


# // tuples 



# t= ("Apple","banana","graps","mango","blueberry")


# n = (10, 20, 30, 40, 50)

# print(n[0])
# print(n[-1])


# s=("prakash","hussain","faiz","faizan","danish")

# for i in range(len(s)):
#     print(s[i])


# n=(5, 2, 5, 8, 5, 10)

# t=n.count(5)


# print(t)


# g=("Java", "C", "Python", "JavaScript")

# i = g.index("Python")

# print(i)


# f=("Apple", "Banana", "Mango")

# b= False

# for i in range(len(f)):
#     if f[i] == "Mango":
#         b= True

# print(b)



# n=(10, 20, 30, 40, 50)

# i=0

# while i < len(n):
#     print(n[i])
#     i +=1


# stu = ("khwaja",22,"11-04-2004")

# name,age,dob=stu

# print(name)
# print(age)
# print(dob)


# f=("Red", "Green", "Blue", "Yellow")

# l = len(f)

# print(l)


# n=(1,2,3,4,5,6,7,8,9,10)

# for i in range(len(n)):
#     if n[i] % 2 ==0:
#         print(n[i])



# SET


# l=[1,2,3,3,3,3,4,5,6,7,7,7,7]

# s= set(l)
# print(s)

# s1={2,3,4,5,6,7}
# s2={2,3,4,5,8,9}

# print(s1 | s2)



# distionaries
# vanilla python
# d = {10:100,20:200,30:300}


# d[40] =400 #create
# d[10] = 10  #update

# print(d.get(20))
# print(d.items())
# print(d.keys())
# # print(d.pop(30))


# # d.popitem()

# d.setdefault(70,2000)

# d.update({80:80000})

# print(d)
# print(d.values())


# traversing (loops)

# question 1


# d= {10:100,20:200,30:300,40:400}
# c = {50:500,60:600}

# d.update(c)

# for i in c:
#     d[i] = c[i]

# sum=0

# for i in c:
#     sum += c[i]

# print(sum)


# frequency counting

# a= ["a","b","a","c","b","a","c","a","b"]

# d={}

# for i in a:
#     if i in d.keys():
#         d[i] = d[i] + 1
#     else:
#         d[i] = 1

# print(d)



# d1= {10:100,20:200,30:300,40:400}
# d2 = {40:500,60:600}


# for i in d2:
#     if i in d1:
#         d1[i] = d1[i] + d2[i]
#     else:
#         d1[i] = d2[i]



# print(d1)










