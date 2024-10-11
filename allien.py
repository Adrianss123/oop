import math
class Ball:
    def __init__(self,diameter):
      self.diameter=diameter
      self.health=120
      self.joy=80
    def volume(self):
       return(math.pi*self.diameter**3)/6
    def meeting(self,energy):
       energy.health-=20
    

class Cube:
   def __init__(self,diameter):
    self.diameter=diameter
    self.health=120
    self.joy=80
   def volume(self):
      return(self.diameter**3)
   
   def meeting(self,energy):
       energy.health-=20
hero1=Ball(5)
print(round(hero1.volume(),2)) 
hero2=Cube(5)
print(hero2.volume()) 
print(hero1.health)
hero1.meeting(hero2)
print(hero2.health)