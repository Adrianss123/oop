class Rectangle:
    def __init__(self,name,width=10,height=20, color='blue'):
      """  self.width=int(input("ievadiet platumu: "))
        self.height=int(input("ievadiet garumu: "))"""
      
      self.width=width
      self.height=height
      self.color=color
      self.name=name
rect1=Rectangle("Square",100,100,"Orange")
print(f"{rect1.width}x{rect1.height}")
rect2=Rectangle('Rect')
rect2.width=20
rect2.height=1245
print(f"{rect2.name} {rect2.color} {rect2.width}x{rect2.height}") 

rectangles=[]
for i in range(100):
    rectangles.append(Rectangle("Name"))
for rect in rectangles:
   print(f"{rect2.name} {rect2.color} {rect2.width}x{rect2.height}") 



































































