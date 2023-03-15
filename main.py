import time
#karma = []
#allignments = ["good", "bad", "evil"]
minutes = 0
meters = 0
energy = 5
choice = False
bus = False
global Start
Start = True

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
   global Start

   if minutes >= 15:
      print("\n You stare down on you watch, and feel your heart dropping.")
      time.sleep(2)
      print("8.30.")
      time.sleep(1)
      print("Your class starts now.")
      time.sleep(2)
      print("I'm sorry " + s.name + "; you didn't make it.")

      Start = False
   
   elif meters >= 25:
      print("\n You see the school slowly appearing in the horizon. You made it!")
      time.sleep(2)
      print("You start running as fast as you can. It feels like hours pass by, but somehow, you walk through the door just in time for your first class.")
      time.sleep(2)
      print("Congratulations " + s.name + "; you made it!")

      Start = False

   return Start

while Start == True:
  print("\n You wake up to an screaming alarm.")
  time.sleep(2)
  print("You put on clothes and run down to the kitchen.")
  time.sleep(2)

  choice = True
  while choice == True:
      print("\n Right when you're about to leave the house, you see a sandwich laying on the table. You hear your stomach growling as you're thinking about what you should do.")
      time.sleep(2)
      choiceAnswer = input(s.name + "; do you want eat the sandwich? \n [Yes] or [No] \n")

      if choiceAnswer.lower() == "yes":
          print("\n You walk up to the table as fast as you can. As you hear your stomach rumbling, you feel like you made the right decision.")
          time.sleep(2)
          print("You grab the sandwich and eat it slowly, while enjoying every single bite.")
          time.sleep(2)
          minutes += 2
          energy += 1
          checkFinish()
          choice = False

      elif choiceAnswer.lower() == "no":
          print("\n You chose to ignore your hunger and keep on walking out of the door.")
          time.sleep(2)
          checkFinish()
          choice = False

      else:
          print("Please choose yes or no.")
          time.sleep(1)

  if Start == False:
     break

  print("\n The sun is shining. You slowly walk down the street, when you see a bus driving on the street in front of you.")
  time.sleep(2)
  print("You suddenly stop as you're watching the bus. Can you make it? Is it worth it?")
  time.sleep(2)

  choice = True
  while choice == True:
      choiceAnswer = input("\n" + s.name + "; Do you want to run and try and catch the bus? \n [Yes] or [No] \n")

      if choiceAnswer.lower() == "yes":
          print("\n You've got no time to lose! You start to run as fast as you can.")
          time.sleep(2)
          print("You get closer to the bus stop. The bus stops and people start to go aboard.")
          time.sleep(2)
          print("Your first day depends on this moment. While thinking that, you speed up.")
          time.sleep(2)

          if energy > 5:
              print("\n You get to the bus and manages to jump on, right before the door closes")
              print("You made it!")
              minutes += 2
              meters += 10
              energy += 2
              bus = True

          else:
              print("\n You get to the bus stop, just to see it driving away from you.")
              time.sleep(2)
              print("Exhausted from the running, you take a deep sigh for yourself.")
              minutes += 4
              meters += 5
              energy -= 2
          
          if checkFinish() == False:
             break
          
          choice = False

      elif choiceAnswer.lower() == "no":
          print("\n You decide that it's not worth it, and continue to walk down the street.")
          minutes += 4
          meters += 5
          energy -= 1

          if checkFinish() == False:
             break
          
          choice = False

      else:
          print("\n Please choose yes or no")

  if Start == False:
     break
  
  if bus == True:
      print("\n You sit on the bus, watching how the landscape is slowly moving.")
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
        choiceAnswer = input("\n" + s.name + "; Do you want to leave the bus or stay in it? \n [Leave] or [Stay] \n")

        if choiceAnswer.lower() == "leave":
          print("\n Just as the bus stops, you run off with no time to lose.")
          time.sleep(2)
          minutes += 4
          meters += 10
          bus = False
          if checkFinish() == False:
             break
          
          choice = False
        
        elif choiceAnswer.lower() == "stay":
          print("\n After thinking for a while, you decide to stay on the bus.")
          time.sleep(2)
          print("You stay on the bus until the final stop, where you chose to go off.")
          minutes += 4
          meters += 5
          energy += 1
          if checkFinish() == False:
             break
          
          choice = False
        
        else:
          print("\n Please choose leave or stay.")
          time.sleep(1)

  if Start == False:
     break
  print("\n You look down on your watch. Oh no! Only " + str(15-minutes) + " minutes left!")
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
    minutes += 3
    energy -= 1
    meters += 10
    
  else:
    print("You feel tired, so you decide to walk a little slower.")
    time.sleep(2)
    print("Maybe you shouldn't have stayed up so late, you think as you walk down the street.")
    time.sleep(2)
    minutes += 3
    energy -= 1
    meters += 5
  
  if checkFinish() == False:
    break

  print("\n While catching your breath, you see a bike in the ditch.")
  time.sleep(2)
  print("It seems like it could work, but is it worth the risk?")
  time.sleep(2)

  choice = True
  while choice == True:
    choiceAnswer = input("\n" + s.name + "; Do you want to take the bike? \n [Yes] or [No] \n")

    if choiceAnswer.lower() == "yes":
        print("\n You approach the bike, and lift the handlebar; it fell off!")
        time.sleep(2)
        print("While taking a closer look, the bike also misses a wheel!")
        time.sleep(2)
        print("You sigh, as you realise that the bike won't work.")
        minutes += 4
        energy -= 1
        if checkFinish() == False:
            break
        
        choice = False
    
    elif choiceAnswer.lower() == "no":
        print("\n You decide that it's not worth the risk, and therefore starts walking away.")
        minutes += 2
        if checkFinish() == False:
            break
        
        choice = False
    
    else:
      print("Please choose yes or no.")
      time.sleep(1)

  if Start == False:
     break
  print("\n You start to feel hopeless. How are you going to make it there in time?")
  time.sleep(2)
  print("You continue to walk for a bit, until you see a sign.")
  time.sleep(2)
  print("In order to get to your school, you can go both ways.")
  time.sleep(2)
  print("Either, you go left. Then you'll have to pass through the woods but the road is slightly shorter.")
  time.sleep(2)
  print("You can also go right. The road is wider and easier to walk, but is a bit longer.")
  time.sleep(2)

  choice = True
  while choice == True:
    choiceAnswer = input("\n" + s.name + "; Do you want to go left or right? \n [Left] or [Right] \n")

    if choiceAnswer.lower() == "left":
        print("\n You've always liked the woods, so you decide to walk in that direction.")
        time.sleep(2)
        print("\n The birds sing and the sun shines. It feels like a perfect day.")
        time.sleep(2)
        print("You feel so relaxed, and the time just flies away.")

        minutes += 2
        energy += 2
        meters += 5

        if checkFinish() == False:
            break
        choice = False

    elif choiceAnswer.lower() == "right":
        print("\n The woods was never for you, so you decide to take right.")
        time.sleep(2)       
        print("\n You walk as fast to make up for the extra distance you had to walk.")
        time.sleep(2)
        print("Even if it's morning, the traffic is calm and there are barely any cars there.")
        time.sleep(2)
        print("You feel relived that it went pretty fast, even if you walked the longer road.")
        time.sleep(2)

        meters += 5
        minutes += 4
  
        if checkFinish() == False:
          break
        choice = False
        
    else:
      print("Please choose left or right.")
      time.sleep(1)
  
  if Start == False:
     break
  
  time.sleep(2)
  print("\n You start to feel lost. Shouldn't you be there yet?")
  time.sleep(2)
  print("You look down on your watch. You only got " + str(15-minutes) + " min left.")
  time.sleep(2)
  print("You start to feel worried. Will you make it there in time?")
  time.sleep(2)
  print("Being late for your first day wouldn't be good.")
  time.sleep(2)
  print("Maybe you should speed up, you wonder as you walk down the road.")
  time.sleep(2)

  choice = True
  while choice == True:
    choiceAnswer = input("\n" + s.name + "; Do you want to run, walk faster or continue to walk in your current pace? \n [Run], [Faster] or [Continue] \n")

    if choiceAnswer.lower() == "run":
       if energy >= 7:
         print("\n You've got no time to lose!")
         time.sleep(2)
         print("You take a deep breath, and then you start to run as fast as you can.")
         time.sleep(2)
         print("It feels like you're flying as you run along the road.")
         time.sleep(2)
         print("After a few minutes, you decide to slow down and go back to your regular pace.")
         time.sleep(2)

         minutes += 4
         energy -= 1
         meters += 10

       else:
          print("\n As you try to start running, your legs start to feel like spagetti.")
          time.sleep(2)
          print("You can't run like this, you think to yourself as you slow down again.")
          time.sleep(2)

          minutes += 4
          energy -= 1
          meters += 4
      
       if checkFinish() == False:
          break
       choice = False

    
    elif choiceAnswer.lower() == "faster":
       if energy >= 5:
          print("\n You've got no time to lose! You think, as you start walking faster.")
          time.sleep(2)
          print("You start to walk as fast as you can.")
          time.sleep(2)
          print("You feel stressed as you try to take as long steps as you can.")
          time.sleep(2)
          print("After a few minutes, you decide to slow down and go back to your regular pace.")
          time.sleep(2)

          minutes += 4
          energy -= 1
          meters += 7
       
       else:
          print("\n As you try to start walking faster, your legs start to feel like spagetti.")
          time.sleep(2)
          print("You can't walk like this, you think to yourself as you slow down again.")
          time.sleep(2)

          minutes += 4
          energy -= 1
          meters += 2
        
       if checkFinish() == False:
          break
       choice = False
    
    elif choiceAnswer.lower() == "continue":
       print("It's not worth it, you think as you continue to walk in your usual pace.")
       print("You will get there in time, you assure yourself.")
    
       minutes += 4
       meters += 5

       if checkFinish() == False:
          break
       choice = False
    
    else:
      print("Please choose run, faster or continue.")
      time.sleep(1)
  
  if Start == False:
    break