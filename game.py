#import main.py
# ATT GÖRA
# koppla ihop tid och meter

import time

minutes = 0
meters = 0
energy = 5
choice = False


print("You wake up to an screaming alarm.")
print("...")

print("You put on clothes and run down to the kitchen.")
time.sleep(2)

choice = True
while choice == True:
    print("Right when you're about to leave the house, you see a sandwich laying on the table. You hear your stomach growling as you're thinking about what you should do.")
    time.sleep(2)
    choiceAnswer = input("Do you eat the sandwich? \n [Yes] or [No] \n")

    if choiceAnswer.lower() == "yes":
        print("You walk up to the table as fast as you can. As you hear your stomach rumbling, you feel like you made the right decision.")
        time.sleep(2)
        print("You grab the sandwich and eat it slowly, while enjoying every single bite.")
        time.sleep(2)
        minutes += 1
        energy += 1
        choice = False

    elif choiceAnswer.lower() == "no":
        print("You chose to ignore your hunger and keep on walking out of the door.")
        time.sleep(2)
        choice = False

    else:
        print("Please choose yes or no.")
        time.sleep(1)

print("\n")
print("The sun is shining. You slowly walk down the street, when you see a bus driving on the street in front of you.")
time.sleep(2)
print("You suddenly stop as you're watching the bus. Can you make it? Is it not worth it?")
time.sleep(2)

choice = True
while choice == True:
    time.sleep(2)
    choiceAnswer = input("Do you want to run and try and catch the bus? \n [Yes] or [No] \n")

    if choiceAnswer.lower() == "yes":
        print("You've got no time to lose! You start to run as fast as you can.")
        time.sleep(2)
        print("You get closer to the bus stop. The bus stops and people start to go aboard.")
        time.sleep(2)
        print("Your first day depends on this moment. While thinking that, you speed up.")
        time.sleep(2)

        if energy > 5:
            print("You get to the bus and manages to jump on, right before the door closes")
            print("You made it!")
            minutes += 1
            meters += 10
        else:
            print("You get to the bus, just to see it driving away from you.")
            time.sleep(2)
            print("Exhausted from the running, you take a deep sigh for yourself.")
            minutes += 1
            meters += 5

        choice = False

    elif choiceAnswer.lower() == "no":
        print("You decide that it's not worth it, and continue to walk down the street.")
        minutes += 1
        meters += 5

        choice = False


    else:
        print("Please choose yes or no")

print("\n")
print("end of story")