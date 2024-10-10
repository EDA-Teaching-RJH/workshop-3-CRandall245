def main():
    perc = int(input("What percentage did you score?"))
    if 100 >= perc and perc <= 90:
        print("Grade: A") 
    elif 89 >= perc and perc <= 80:
        print("Grade: B")
    elif 79 >= perc and perc <= 70:
        print("Grade: C")
    elif 69 >= perc and perc <= 60:
        print("Grade: D")
    elif 59 >= perc:
        print("Grade: F")
    else:
        print("Error")

main()
