class vertebrate:
    def __init__(self, backbone=True):
        self.has_backbone=backbone
    def vertebrate_info(self):
        print(f"vertebrates have a backbone")

class aquatic:
    def __init__(self, habitat="water"):
        self.habitate=habitat
    def aquatic_info(self):
        print(f"aquatic animals live in water")

class fish(vertebrate,aquatic):
    def __init__(self, species, backbone=True, habitat="water"):
        super().__init__(backbone=backbone)
        self.habitate=habitat
        self.species=species

    def fish_info(self):
        print(f"The {self.species} is a type of wish that lives in {self.habitate}")

    def swim(self):
        print(f"the fish is swimming")

goldfish=fish("goldfish")
print(goldfish.has_backbone)
goldfish.swim()
