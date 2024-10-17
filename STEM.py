from random import*
class STEM:
    def rectangle_area(width=0, height=0):
        if width>0 and height>0:
           print(f'The area is {abs(width)*abs(height)}')
        else:
            print(f'Can not calculate negative area {width}x{height}')


for i in range(20):
    w=randint(-20,20)
    h=randint(-20,20)
    STEM.rectangle_area(w,h)
STEM.rectangle_area(20,30)
STEM.rectangle_area(15,20)
STEM.rectangle_area(-10,20) 