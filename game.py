import random

com = random.randint(1,100)
tries = 0



while tries <= 5:

    user = int(input("Enter your number inbetween 1 - 100 : "))
    tries += 1
    if tries == 5:
        print("No more chance left sorry !!")
        break
    elif com == user:
        print(f"Congratulations !! you won in {tries}")
        break
    elif com < user:
        print("close to it goo more down")
    elif com > user:
        print("close to it goo more up")
    else:
        print("no more chance remaining ")



