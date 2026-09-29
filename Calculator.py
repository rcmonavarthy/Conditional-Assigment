loopreq = "y"

print("Hi! Let's do some math.")

print("")

while loopreq == "y":
    try:
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        num3 = int(input("Enter third number: "))

        sum1 = num1 + num2 + num3

        if sum1 > 0:
            print("The sum is positive.")

        if sum1 < 0:
            print("The sum is negative.")

        if sum1 == 0:
            print("The sum is zero.")
        continue
    except ValueError:
        print("Please enter a number.")
    finally:
        loopreq = input("Would you like to use the program again? (y/n) ")
if loopreq == "n":
    input("Goodbye! Press enter to exit.")
