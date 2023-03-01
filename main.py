karma = []
allignments = ["good", "bad", "evil"]
game_bool = True


class StartScreen():
  def __init__(self, name, age, moralAllignment):
    self.name = name
    self.age = age
    self.moralAllignment = moralAllignment

def StartMenu():
  StartScreen.age = int(input("How old are you (in the game)?: "))
  StartScreen.name = str(input("What is your name (in the game)?: "))
  print(allignments)
  StartScreen.moralAllignment = str(input("What allginment do you want? (choose from the above): ")).lower()

  if StartScreen.moralAllignment == allignments[0]:
    karma.append(10)
  if StartScreen.moralAllignment == allignments[1]:
    karma.append(0)
  if StartScreen.moralAllignment == allignments[2]:
    karma.append(-10)

  if StartScreen.age > 99:
    StartScreen.age = input(int("How old are you (in the game)?: "))
  if len(name) > 10:
    name = input(str("What is your name (in the game)?: "))  
  
s = StartScreen(0, 0, 0)

while game_bool == True:
  StartMenu()
  if s.StartMenu() == False:
    game_bool = False
