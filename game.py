#import main.py
# ATT GÖRA
# koppla ihop tid och meter

import time

minutes = 0
meters = 0
choice = False


print("You wake up to an screaming alarm.")
print("...")

choice = True
while choice == True:
    print("You put on clothes and run down to the kitchen.")
    time.sleep(2)
    print("Right when you're about to leave the house, you see a sandwich laying on the table. You hear your stomach growling as you're thinking about what you should do.")
    time.sleep(2)
    choiceAnswer = input("Do you eat the sandwich? \n [Yes] or [No] \n")

    if choiceAnswer.lower() == "yes":
        print("You walk up to the table as fast as you can. As you hear your stomach rumbling, you feel like you made the right decision.")
        time.sleep(2)
        print("You grab the sandwich and eat it slowly, while enjoying every single bite.")
        time.sleep(2)
        minutes = 1
        choice = False

    elif choiceAnswer.lower() == "no":
        print("You chose to ignore your hunger and keep on walking out of the door.")
        time.sleep(2)
        choice = False

    else:
        print("Please choose yes or no.")
        time.sleep(1)

print("The sun is shining.")