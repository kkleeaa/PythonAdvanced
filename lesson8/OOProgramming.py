


class Rectangle: #defined a class
    def __init__(self,length,width): #konstruktori i klases
        self.length=length #variblat brenda klases
        self.width=width
    def calculate_area(self):
        return self.length*self.width
    def calculate_perimeter(self):
        return 2*(self.length+self.width)

katrori= Rectangle(2,5)
syprina=katrori.calculate_area()
print(syprina)

perimetri=katrori.calculate_perimeter()
print(perimetri)





