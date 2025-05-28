#Simple Unit Converter for weight, height and temperature

from colorama import init, Fore
init(Fore)

print(Fore.LIGHTBLACK_EX + "  _    _       _ _      _____                          _            ")
print(Fore.LIGHTBLACK_EX + " | |  | |     (_) |    / ____|                        | |           ")
print(Fore.LIGHTBLACK_EX + " | |  | |_ __  _| |_  | |     ___  _ ____   _____ _ __| |_ ___ _ __ ")
print(Fore.LIGHTBLACK_EX + " | |  | | '_ \| | __| | |    / _ \| '_ \ \ / / _ \ '__| __/ _ \ '__|")
print(Fore.LIGHTBLACK_EX + " | |__| | | | | | |_  | |___| (_) | | | \ V /  __/ |  | ||  __/ |   ")
print(Fore.LIGHTBLACK_EX + "  \____/|_| |_|_|\__|  \_____\___/|_| |_|\_/ \___|_|   \__\___|_|   ")

print("")

print("[1] Weight")
print("[2] Height")
print("[3] Temperature")

userOption = int(input("Please enter an option: \n"))

if userOption == 1:
    print("You chose to convert your weight!")
    userVal = float(input("Please enter your weight: "))
    print(f"Your weight in kilograms is: {userVal * 0.453592}")
elif userOption == 2:
    print("You chose to convert your height!")
    userFt = int(input("Enter how tall you are (in feet): "))
    userIn = int(input("Enter how tall you are (in inches): "))
    userHeight = (userFt * 30.48) + (userIn * 2.54)
    print(f"You are {userHeight} cm tall!")
elif userOption == 3:
    print("You chose to convert temperature!")
    print("[1] C to F")
    print("[2] F to C")
    userOption = int(input("Please enter an option: "))
    if userOption == 1:
        print("You chose to convert from Celsius to Farenheit!")
        userTemp = float(input("Please Enter Celsius: "))
        farConv = (userTemp * 9/5) + 32
        print(f"In Farenheit, the temperature is: {farConv}")
    elif userOption == 2:
        print("You chose to convert from Farenheit to Celsius")
        userTemp = float(input("Please Enter Farenheit: "))
        celConv = (userTemp - 32) * 5/9
        print(f"In Farenheit, the temperature is: {celConv}")
    else:
        print("You didn't enter a valid option.. try again!")
else:
    print("You didn't enter a valid option.. try again!")