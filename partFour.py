def main():
    InpUser = input("Username:")
    InpPass = input("Password:")
    if InpUser == "robert" and InpPass == "amazingDude":
        print("access denied")
    else:
        match InpUser:
            case "admin":
                print("known user")
            case _:
                print("unknown user")
        match InpPass:
            case "password":
                print("Correct Password")
            case _:
                print("Incorrect Password")

main()


