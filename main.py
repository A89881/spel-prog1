import time
#karma = []
#allignments = ["good", "bad", "evil"]
minutes = 0
meters = 0
energy = 5
choice = False
bus = False
#Start = True

class StartScreen():
  def __init__(self, name, age, moralAllignment):
    self.name = name
    self.age = age
    self.moralAllignment = moralAllignment

  def StartMenu(self):
    self.name = str(input("What is your name (in the game)?: "))

    ageCheck = True
    while ageCheck == True:
      try:
        self.age = int(input("How old are you (in the game)?: "))
        ageCheck = False

      except:
        print("Please choose a number.")

    #print(allignments)
    #self.moralAllignment = str(input("What allginment do you want? (choose from the above): ")).lower()

    #if self.moralAllignment == allignments[0]:
      #karma.append(10)
    #if self.moralAllignment == allignments[1]:
      #karma.append(0)
    #if self.moralAllignment == allignments[2]:
      #karma.append(-10)

    #if self.age > 99:
     # self.age = input(int("How old are you (in the game)?: "))
    #if len(self.name) > 10:
     # self.name = input(str("What is your name (in the game)?: "))  

  def info(self):
    print(f"Your Character; Name: {self.name} Age: {self.age} Moralallignment: {self.moralAllignment}  ")
    #Karma:{str(sum(karma))}

  def Text(self):
    print(f"\nHello {self.name}! You have a class in 15min, come to class in time or you will lose the game")
  
s = StartScreen(0, 0, 0)
s.StartMenu()
s.Text()
time.sleep(2)

def checkFinish():
   if minutes >= 15:
      print("You stare down on you watch, and feel your heart dropping.")
      time.sleep(2)
      print("8.30.")
      time.sleep(1)
      print("Your class starts now.")
      time.sleep(2)
      print("I'm sorry " + s.name + "; you didn't make it.")
   
   elif meters >= 25:
      print("You see the school slowly appearing in the horizon. You made it!")
      time.sleep(2)
      print("You start running as fast as you can. It feels like hours pass by, but somehow, you walk through the door just in time for your first class.")
      time.sleep(2)
      print("Congratulations " + s.name + "; you made it!")

print("You wake up to an screaming alarm.")
time.sleep(2)
print("You put on clothes and run down to the kitchen.")
time.sleep(2)

choice = True
while choice == True:
    print("Right when you're about to leave the house, you see a sandwich laying on the table. You hear your stomach growling as you're thinking about what you should do.")
    time.sleep(2)
    choiceAnswer = input(s.name + "; do you want eat the sandwich? \n [Yes] or [No] \n")

    if choiceAnswer.lower() == "yes":
        print("You walk up to the table as fast as you can. As you hear your stomach rumbling, you feel like you made the right decision.")
        time.sleep(2)
        print("You grab the sandwich and eat it slowly, while enjoying every single bite.")
        time.sleep(2)
        minutes += 2
        energy += 1
        checkFinish()
        choice = False

    elif choiceAnswer.lower() == "no":
        print("You chose to ignore your hunger and keep on walking out of the door.")
        time.sleep(2)
        checkFinish()
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
    choiceAnswer = input(s.name + "; Do you want to run and try and catch the bus? \n [Yes] or [No] \n")

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
            minutes += 2
            meters += 10
            energy += 2
            bus = True

        else:
            print("You get to the bus, just to see it driving away from you.")
            time.sleep(2)
            print("Exhausted from the running, you take a deep sigh for yourself.")
            minutes += 2
            meters += 5
            energy -= 2
        
        checkFinish()
        choice = False

    elif choiceAnswer.lower() == "no":
        print("You decide that it's not worth it, and continue to walk down the street.")
        minutes += 2
        meters += 5
        energy -= 1

        checkFinish()
        choice = False

    else:
        print("Please choose yes or no")

if bus == True:
    print("You sit on the bus, watching how the landscape is slowly moving.")
    time.sleep(2)
    print("As you  tilt your head back, you feel your eyelids getting more and more heavy...")
    time.sleep(2)
    print("!!!")
    time.sleep(1)
    print("You fell asleep!")
    time.sleep(2)
    print("And you missed your stop!")
    time.sleep(2)
    print("What do you do now? Do you leave the bus at the next stop, or do you want to continue to see where it takes you?")
    time.sleep(1)

    choice = True
    while choice == True:
      choiceAnswer = input(s.name + "; Do you want to leave the bus or stay in it? \n [Leave] or [Stay] \n")

      if choiceAnswer.lower() == "leave":
        print("Just as the bus stops, you run off with no time to lose.")
        time.sleep(2)
        minutes += 2
        meters += 10
        bus = False
        checkFinish()
        choice = False
      
      elif choiceAnswer.lower() == "stay":
        print("After thinking for a while, you decide to stay on the bus.")
        time.sleep(2)
        print("You stay on the bus until the final stop, where you chose to go off.")
        minutes += 2
        meters += 5
        energy += 1
        checkFinish()
        choice = False
      
      else:
        print("Please choose leave or stay.")
        time.sleep(1)



if bus == False:
  print("You look down on your watch. Oh no! Only " + str(15-minutes) + " minutes left!")
  time.sleep(2)
  print("Feeling more and more stressed, you start walking faster.")
  time.sleep(2)

  if energy >= 6:
     print("You feel energized, so you decide to start running.")
     time.sleep(2)
     print("With the wind blowing in your hair, you feel more and more free.")
     time.sleep(2)
     print("After a while, you slow down and start to breath heavy.")
     time.sleep(2)
     minutes += 2
     energy -= 1
     meters += 10
    
  else:
     print("You feel tired, so you decide to walk a little slower.")
     time.sleep(2)
     print("Maybe you shouldn't have stayed up so late, you think as you walk down the street.")
     time.sleep(2)
     minutes += 2
     energy -= 1
     meters += 5
  
  checkFinish()

  print("While catching your breath, you see a bike in the ditch.")
  time.sleep(2)
  print("It seems like it could work, but is it worth the risk?")
  time.sleep(2)

  choice = True
  while choice == True:
    choiceAnswer = input(s.name + "; Do you want to take the bike? \n [Yes] or [No] \n")

    if choiceAnswer.lower() == "yes":
        print("You approach the bike, and lift the handlebar; it fell off!")
        time.sleep(2)
        print("While taking a closer look, the bike also misses a wheel!")
        time.sleep(2)
        print("You sigh, as you realise that the bike won't work.")
        minutes += 2
        energy -= 1
        checkFinish()
        choice = False
    
    elif choiceAnswer.lower() == "no":
        print("You decide that it's not worth the risk, and therefore starts walking away.")
        minutes += 2
        checkFinish()
        choice = False
    
    else:
      print("Please choose yes or no.")
      time.sleep(1)

print("\n")
print("end of story")