from abc import ABC, abstractmethod

class Person (ABC):
    def __init__(self, name,age,height,weight):
        self.name=name
        self.age=age
        self.height=height
        self.weight=weight
    @property
    def name(self):
        return self._name
    @property
    def age(self):
        return self._age
    @property
    def height(self):
        return self._height
    @property
    def weight(self):
        return self._weight
    @abstractmethod
    def calculate_bmi(self):
        pass
    @abstractmethod
    def get_bmi_category(self):
        pass
    def print_info(self):
        bmi=self.calculate_bmi()
        category=self.get_bmi_category()
        print(f"Name:{self.name}, Age:{self.age}, Height:{self.height}, Weight:{self.weight}")
class adult(Person):
    def calculate_bmi(self):
        return self.weight \ (self.height ** 2)
    def get_bmi_category(self):
        bmi= self.calculate_bmi()
        if bmi 

