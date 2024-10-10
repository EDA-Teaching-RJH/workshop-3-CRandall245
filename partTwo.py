import random

def main():
    obj = random.randint(1, 10)
    loop = True
    while loop == True:
        user_inp = int(input("Guess a number:"))
        if user_inp < obj:
            print("too low")
        elif user_inp > obj:
            print("too high")
        else:
            print("correct")
            loop = False

main()
