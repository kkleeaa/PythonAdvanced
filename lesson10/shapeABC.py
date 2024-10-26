from abc import ABC, abstractmethod

class shape(ABC):
    @abstractmethod
    def area(self):
        pass

class circle (shape):
    def __init__(self,rrezja):
        self.rrezja=rrezja

    def area(self):
        return 3.14 * self.rrezja*self.rrezja

class square(shape):
    def __init__(self,length):
        self.length=length
    def area(self):
        return self.length*self.length

rrethi=circle(3)
katrori=square(4)
print(rrethi.area())
print(katrori.area())





