def main():
    week = input("What day of the week is it?")
    if week == "Saturday" or week == "Sunday":
        print("Its the weekend")
    elif week == "Monday" or week == "Tuesday" or week == "Wednesday" or week == "Thursday" or week == "Friday":
        print("Its a weekday")
    else:
        print("error")

main()
