class Circle :
    pi=22/7
    def __init__(self,radius):
        self.radius=radius

    
    def getArea(self):
        return(self.radius*self.radius*Circle.pi)
    def getCircumference(self):
        return(2*Circle.pi*self.radius)

circ=Circle(int(input("enter the raduis:")))

area= circ.getArea()
perimeter= circ.getCircumference()


print("Area: {}".format(area))
print("Perimeter: {}".format(perimeter))
