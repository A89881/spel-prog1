karma = []
allignments = ["good", "bad", "evil"]

class StartScreen():
  def __init__(self, name, age, moralAllignment):
    self.name = name
    self.age = age
    self.moralAllignment = moralAllignment

  def StartMenu(self):
    self.age = input(int("How old are you (in the game)?: "))
    self.name =input(str("What is your name (in the game)?: "))
    print(allignments)
    self.moralAllignment = input(str("What allginment do you want? (choose from the above): ")).lower()

    try:
      if self.moralAllignment == allignments[0]:
        karma.append(10)
      if self.moralAllignment == allignments[1]:
        karma.append(0)
      if self.moralAllignment == allignments[2]:
        karma.append(-10)
    
    except:
      print("You failed to understand the game")

    def StoryInformation(self):
      
      pass

    