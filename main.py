karma = []
allignments = ["good", "bad", "evil"]
meters = 0
time = 0
Start = True


class StartScreen():
  def __init__(self, name, age, moralAllignment):
    self.name = name
    self.age = age
    self.moralAllignment = moralAllignment

  def StartMenu(self):
    self.age = int(input("How old are you (in the game)?: "))
    self.name = str(input("What is your name (in the game)?: "))
    print(allignments)
    self.moralAllignment = str(input("What allginment do you want? (choose from the above): ")).lower()

    if self.moralAllignment == allignments[0]:
      karma.append(10)
    if self.moralAllignment == allignments[1]:
      karma.append(0)
    if self.moralAllignment == allignments[2]:
      karma.append(-10)

    if self.age > 99:
      self.age = input(int("How old are you (in the game)?: "))
    if len(self.name) > 10:
      self.name = input(str("What is your name (in the game)?: "))  

  def info(self):
    print(f"Your Character; Name: {self.name} Age: {self.age} Moralallignment: {self.moralAllignment} Karma:{str(sum(karma))} ")

  def Text(self):
    print(f"\n Hello {self.name}! You have a class in 15min")
  
s = StartScreen(0, 0, 0)
while Start == True:
  pass
