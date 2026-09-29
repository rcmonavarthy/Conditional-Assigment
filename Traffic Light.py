loopreq = "y"

while loopreq == "y":
    print("Welcome to the Traffic Light Program")

    print("")

    color = input("What color is the traffic light? ")

    if color == "red":
        print("The traffic light is red, so you must stop before the white line.")
    if color == "green":
        print("The traffic light is green, so you may proceed through the intersection.")
    if color == "yellow":
        print("The traffic light is yellow, which means it will turn red shortly. You should slow down and prepare to stop")

    if color not in ("green", "red", "yellow"):
        print("The color is invalid. Please try again.")

    print("")

    loopreq = input("Would you like to use the Traffic Light Program again? (y/n) ")

if loopreq == "n":
    input("Goodbye! Press enter to exit.")