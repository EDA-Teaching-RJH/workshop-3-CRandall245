def main():
    age = input(int("How old are you?"))
    stud = input("Are you a student? Y/N")
    if age < 12 or age > 64:
        print("That will cost £5")
    elif stud == "Y":
        print ("That will cost £8")
    elif age > 12 and age < 65 and stud == "N":
        print ("that will cost £10")
    else:
        print("error")

main()