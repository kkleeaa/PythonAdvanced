from abc import ABC, abstractmethod
from gettext import npgettext


class person(ABC):
    def __init__(self,name,age,height, weight):
        self.name=name
        self.age=age
        self._weight=weight
        self._height=height
    @property
    def weight(self):
        return self._weight

    @weight.setter
    def weight(self,value):
        if value<0:
            raise ValueError("Weight cannot be negative")
        self._weight=value

    @property
    def height(self):
        return self._height
    @height.setter
    def height(self,value):
        self._height=value

    @abstractmethod
    def calculate_bmi(self):
        pass
    @abstractmethod
    def get_bmi_category(self):
        pass
    def print_info(self):
        print(f"Name:{self.name}, Age:{self.age},Weight:{self.weight}kg, Height:{self.height}cm")
        print(f"bmi: {self.calculate_bmi():.2f}, Category:{self.get_bmi_category()}")

class Adult(person):
    def calculate_bmi(self):
        return self.weight/(self.height**2)
        def get_bmi_category(self):
            bmi=self.calculate_bmi()
            if bmi <18.5:
                return "Underweight"
            elif 18.5<=bmi<24.9:
                return "Normal Weight"
            elif 24.9<=bmi<29.9:
                return "Overweight"
            else:
                return "obese"

class child(Adult):
    def get_bmi_category(self):
        def get_bmi_category(self):
            bmi=self.calculate_bmi()*1.3
            if bmi <14:
                return "Underweight"
            elif 14<=bmi<18:
                return "Normal Weight"
            elif 18<=bmi<24:
                return "Overweight"
            else:
                return "obese"
class BMIapp:
    def __init__(self):
        self.people=[]
    def add_person(self,person):
        self.people.append(person)
    def collect_user_data(self):
        name=input("Enter name")
        age=int(input("Enter age"))
        weight=float(input("Enter weight in kg:"))
        height=float(input("Enter height in m:"))
        if age>=18:
            person=Adult(name,age,weight,height)
        else:
            person=child(name,age, height, weight)
        self.add_person(person)
    def print_result(self):
        for person in self.people:
            person.print_info()
    def run(self):
        while True:
            self.collect_user_data()
            cont=input("Do you want to add a person").strip().lower()
            if cont!='y':
                break
        self.print_result()

app=BMIapp()
app.run()

import numpy as np
arr_2d=np.array([[1,2,3,54],[4,5,6,88]])
print(arr_2d)






