class Student:
    def __init__(self, name, course, notamesatare):
        self._notamesatare= notamesatare
        self.name=name
        self.course=course
    def greet(self):
        print(f"Hello i am {self.name} and i practice {self.course}")

    def _tregonnota(self):
        print("this is a protected method")


Klea=Student("Klea","Python","5")
Klea.greet()



