def main():
    perc = int(input("What percentage did you score?"))
    if perc > 101 and perc < 89:
        print("Grade: A") 
    elif perc <= 89 and perc >= 80:
        print("Grade: B")
    elif perc <= 79 and perc >= 70:
        print("Grade: C")
    elif perc <= 69 and perc >= 60:
        print("Grade: D")
    elif perc <= 59:
        print("Grade: F")
    else:
        print("Error")

main()
