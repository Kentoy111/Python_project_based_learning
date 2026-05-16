import math
while True:
    print("")
    print("-----CALCULATOR APP-----")
    print("--Calculator Features-- \n|+ = Addition       |\n|- = Subtraction    |\n|* = Multiplication |\n|/ = Division       |")
    user_input1 = int(input("Type the first number: "))
    operations = input("Operation to be used: ")
    user_input2 = int(input("Type the second number: "))
    user_option = input("Do you wish to continue(Y/n): ").lower()
    if user_option == "n":
        break
    def Calculation():
        if operations == "+":
            return user_input1 + user_input2
        elif operations == "-":
            return user_input1 - user_input2
        elif operations == "/":
            try:
                return user_input1 / user_input2
            except ZeroDivisionError:
                print("Error: Cannot be divided by zero")    
        elif operations == "*":
            return user_input1 * user_input2
        else:
            print("Wrong operation please try again")

    display = Calculation()
    print(f"Answer:{display}")