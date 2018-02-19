class RectangleGeometry :
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def getArea(self):
        return(self.length*self.breadth)
    def getperimeter(self):
        return(2*(self.length+self.breadth))

rect=RectangleGeometry(int(input("enter the length")),int(input("enter the breadth")))

area=rect.getArea()
perimeter=rect.getperimeter()
    
print("Area = {}".format(area))
print("Perimeter = {}".format(perimeter))
