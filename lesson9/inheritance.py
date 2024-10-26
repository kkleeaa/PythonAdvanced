class animal:
    def __init__(self,name):
        self.name=name

    def sound(self):
        print("some generic animal sound")

    def description(self):
        print(f"This animals name is {self.name}")


class dog(animal):
    def __init__(self,name,breed):
        super().__init__(name)
        self.breed=breed

    def sound(self):
        print("WOOF WOOF")

    def description(self):
        super().description()
        print(f"This is the breed ,{self.breed}")



class cat(animal):
    def __init__(self,name):
        super().__init__(name)

    def sound(self):
        print("Meow Meow")

kafsha=animal("generic name")
kafsha.sound()

qeni=dog('rex',"labrador")

qeni.sound()

maca=cat("whiskers")
maca.sound()
qeni.description()





