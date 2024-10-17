import random 


class Rectangle:
    count=0
    def __init__(self,name,width=10,height=20,color='blue'):
    
        self.width=width
        self.height=height
        self.color=color
        self.name=name
        Rectangle.count+=1
    def inform_count():
        print(f'Instancescreated: {Rectangle.count}')
    def introduce(self):
        print(f'{
self.name
}{self.color} {self.width}x{self.height}')
    def calculate_area(self):
        print(f'The area is {self.width*self.height}')

'''
        self.width=int(input("ievadiet platumu: "))
        self.height=int(input("ievadiet garumu: "))
    '''   
rect1=Rectangle('Saquare',100,100,'Orange')
print(f'{
rect1.name
} {rect1.color} {rect1.width}x{rect1.height}')
rect1.calculate_area()
rect2=Rectangle('Rect')
print(f'{
rect2.name
} {rect2.color} {rect2.width}x{rect2.height}')
rect2.calculate_area()

rectangles=[]
colors=['red','orange','green','blue', 'yellow']
for i in range(100):
    rectangles.append(Rectangle(f'Name{i+1}', random.randint(1,500), random.randint(1,500), random.choice(colors) ))

for rect in rectangles:
    print(f'{
rect.name
} {rect.color} {rect.width}x{rect.height}')
   # print(rect)
print(Rectangle.count)
Rectangle.inform_count() 