# Define the base classplayer
class player:
 def __init__(self):
  def play(self):
    print("The player isplaying cricket.")
# Define the derived class batsman
class batsman(player):
  def play(self):
    print("The batsman is batting")
# Define the derived class bowler
class bowler(player):
 def play(self): 
   print("The bowler is bowling")
# create objects ofbatsman and bowler classes
b1=batsman() 
b2=bowler()
# call the play() methodfor each object
b1.play()  
b2.play()