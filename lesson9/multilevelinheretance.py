class vehicle:
    def __init__(self, make,model,year):
        self.make=make
        self.model=model
        self.year=year
    def display_info(self):
        print(f"make: {self.make}, model:{self.model}, year:{self.year}")

class car(vehicle):
    def __init__(self, make,model,year,body_style):
        super().__init__(make,model,year)
        self.body_style=body_style

class electriccar(car):
    def __init__(self, make,model,year,body_style, battery_capacity):
        super().__init__(make,model,year,body_style)
        self.battery_capacity=battery_capacity

    def charge(self):
        print(f"charging the electric car")

tesla= electriccar("tesla","cybertruck","2023","triangular","112.4")
print(tesla.charge())

