from random import*
class Rectangle:
    def __init__(self,name,width=0,height=0,color='green'):
        self.width=width
        self.height=height
        self.name=name
        self.color=color
rect1=Rectangle("rectangle",100,3141)
print(f"{rect1.name} {rect1.width}x{rect1.height} {rect1.color}")
rect2=Rectangle("sqwar3e")
print(f"{rect2.name} {rect2.width}x{rect2.height} {rect2.color}")
rectan=[]
colors=['red','orange','green','blue','yellow', 'purple']
for i in range(100):
        rectan.append(Rectangle(f"Name{i+1}",randint(1,500), randint(1,500) ,
      choice(colors)))
for rect in rectan:
    print(f"{rect.name} {rect.width}x{rect.height} {rect.color}") 
