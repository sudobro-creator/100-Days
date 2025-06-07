print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/
*******************************************************************************
''')

print("Welcome to Treasure Island!")
print("Your mission is to find the treasure.")

choice1 = input("You're at a crossroad. Do you want to go left or right? ").lower()
if choice1 == "right":
    choice2 = input("You've come to a lake. Do you want to swim or wait for a boat? ").lower()
    if choice2 == "swim":
        choice3 = input("You arrive at the island unharmed. There is a house with three doors. Do you choose red, blue, or yellow? ").lower()
        if choice3 == "red":
            print("Congratulations! You found the treasure! 🏆")
        elif choice3 == "yellow":
            print("You were burned by sun. Game Over. ☀️")
        elif choice3 == "blue":
            print("You were eaten by bees. Game Over. 🪰")
        else:
            print("You chose a door that doesn't exist. Game Over. 🚪")
    else:
        print("You got killed by some bad boys. Game Over. 🔫")
else:
    print("You fell into a hole. Game Over. 🕳️")    