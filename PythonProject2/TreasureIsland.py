print(r'''
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
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.\n")
print("You come to a fork in the road.")
choice_1 = input("Would you like to go left or right?\n").lower()

if choice_1 == "left":
    print("You follow the left path and come to a strong flowing river.")
    choice_2 = input("Would you like to take your chances and swim or wait for the river to die down?\n").lower()
    if choice_2 == "wait":
        print("You choose to wait for the river to die down.")
        print("While waiting for the river to die down, a set of doors materialise.")
        print("There is a yellow door, a red door, and a blue door.")
        choice_3 = input("Which door do you try?\n").lower()
        if choice_3 == "yellow":
            print("You choose to go through the yellow door.")
            print("You see a room full of endless gold and jewels.")
            print("YOU WIN!")
        elif choice_3 == "red":
            print("You enter the red door.")
            print("The door slams behind you locked.")
            print("The room ignites in an instant.")
            print("You burned to death.")
            print("GAME OVER!")
        elif choice_3 == "blue":
            print("You enter a room that has an uninviting smell.")
            print("The door slams shut, as you hear growls coming from the darkness.")
            print("An endless onslaught of magical beasts attack you.")
            print("GAME OVER!")
        else:
            print("You spontaneously implode.")
            print("GAME OVER!")
    else:
        print("You choose to take your chances, and start swimming.")
        print("A trout attacks you while you're swimming.")
        print("GAME OVER!")
else:
    print("You take the right path and don't notice a false floor.")
    print("You fall to your death.")
    print("GAME OVER!")
