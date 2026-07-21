import random
while True:
    user = int(input("Enter your action 1-Rock || 2-Paper || 3-Scissor :- "))
    comp = random.randint(1,3)
    print(comp)
    if user == comp:
        print("congratulations you won the game")
        break
    elif user in range(4,10):
        print("Please select correct number")
    else:
        print("You Loss !!")