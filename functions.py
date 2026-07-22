# def greet(name):
#     print(name)

# greet("khwaja")


# def addNum(a,b):
#     return a+b

# print(addNum(10,5))


# def checkNum(num):
#     if num % 2 == 0:
#         print("Even")
#     else:
#         print("Odd")



# checkNum(9)


# def lNum(a,b,c):
#     print(max(a,b,c))


# lNum(20,55,40)


# def findSqr(n):
#     return n ** 2

# print(findSqr(7))


# def countVowels(word):
#     count = 0
#     for i in word.lower():
#         if i in "aeiou":
#             count += 1
    
#     if count == 0:
#         print("No vowels found")
#     else:
#         print(count)



# countVowels("python")





# def checkVowels(word):

#     count = 0
#     for i in word.lower():
#         if i in "aeiou":
#             count +=1

#     if count == 0:
#         print("no vowels found")
#     else:
#         print(count)

# checkVowels("python")



# def revStr(word):
#     rev= ""
#     for i in word:
#         rev= i + rev
#     print(rev)


# revStr("hello")



# def fac(n):
#     if n < 0:
#         print("Factorial does not exist for negative numbers")

#     fac=1

#     for i in range(1,n+1):
#        fac *= i 

#     print(fac)

# fac(5)






# def findFac(n):

#     fac = 1
#     for i in range(1, n+1):
#         fac *= i
#     print(fac)

# findFac(5)


# def findPrime(n):

#     count = 0

#     for i in range(1, n+1):
#         if n % i == 0:
#             count +=1
#     if count == 2:
#         print("Prime number")
#     else:
#         print("Not a prime number ")

# findPrime(13)



# def findP(n):
#     count = 0

#     for i in range(1,n+1):
#         if n % i == 0:
#             count +=1
    
#     if count == 2:
#         print("Prime")
#     else:
#         print("Not prime")

# findP(6)


def cal(n1,n2,s):
    
    if s == "+":
        return n1 + n2
    elif s == "-":
        return n1 - n2
    elif s == "*":
        return n1 * n1
    elif s == "/":
        return n1 / n2
    else:
        print("No number found")

print(cal(20, 5, "/"))




# --------------------------------------pending 

# Write functions for:

# Find the minimum number in a list.
# Find the maximum number in a list.
# Count the digits in a number.
# Check if a string is a palindrome.
# Generate the first n Fibonacci numbers.














