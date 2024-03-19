import random
ans = input("Would you like to use the dice: ")
response = "y"
if ans == "yes" or "Yes":   
    while response == "y":
        response = input("press y to roll, n to forfeit: ")
        if response == "y":
            num = random.randint(1,6)
            if num == 1:
                print(" 0 ")
            elif num == 2:
                print("0 0")
            elif num == 3:
                print("0 0 0")
            elif num == 4:
                print("0   0")
                print("  0")
                print("0   0")
            elif num == 5:
                print("0   0")
                print("  0")
                print("0   0")
            elif num == 6:
                print("0 0 0")
                print("0 0 0")

else: 
    print("Ok, thank you.")
 