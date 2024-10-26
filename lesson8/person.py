class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def greet(self):
        print(f"Hello, i am {self.name} and i am {self.age} years old")

person1= person("Klea", 17)
person2= person("Alma",20)

person1.greet()
person2.greet()


