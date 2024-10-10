def main():
    loop = True
    while loop == True:
        num1 = int(input("Give me a number:"))
        num2 = int(input("Give me a number:"))
        op = input("Give me an operator or type quit:")
        match op:
            case "+":
                print("The answer is " , (num1 + num2))
            case "-":
                print("The answer is " , (num1 - num2))
            case "/":
                print("The answer is " , (num1 / num2))
            case "*":
                print("The answer is " , (num1 * num2))
            case "^":
                print("The answer is " , (num1 ** num2))
            case "%":
                print("The answer is " , (num1 % num2))
            case "quit":
                loop = False

main()
