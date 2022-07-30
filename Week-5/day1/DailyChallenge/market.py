class Farm():
    def __init__(self, name):
        self.animals = []
        self.name = name

    def add_animal(self, new_animal):
        self.animals.append(new_animal)

    # def get_Info(self):


macdonald = Farm("Mcdonald")
macdonald.add_animal("cow")
macdonald.add_animal("sheep")
macdonald.add_animal("sheep")
macdonald.add_animal("goat")
# print(macdonald.get_Info())
