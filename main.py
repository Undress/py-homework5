import operator

class Animal:
    animal_name = ""
    animal_type = ""
    weight = 0
    color = ""
    leg_count = 0
    voice = ""
    fed = False
    _instances = {}


    def __init__(self, name, type, weight):
        self.animal_name = name
        self.animal_type = type
        self.weight = weight
        self._instances[name] = weight

    def set_name(self, name):
        self.animal_name = name

    def get_name(self):
        return self.animal_name

    def set_name(self, type):
        self.animal_type = type

    def get_name(self):
        return self.animal_type

    def set_weight(self, weight):
        self.weight = weight

    def get_weight(self):
        return self.weight

    def set_color(self, color):
        self.color = color

    def get_color(self):
        return self.color

    def set_leg_count(self, leg_count):
        self.leg_count = leg_count

    def get_leg_count(self):
        return self.leg_count

    def set_voice(self, voice):
        self.voice = voice

    def get_voice(self):
        return self.voice


    def feed(self):
        self.fed = True
        print("{} is fed\n".format(self.animal_name))



class Bird(Animal):

    leg_count = 2
    eggs_count = 0

    def lay_eggs(self, count):
        self.eggs_count += count
        print("{} {} gave {} eggs\n".format(self.animal_type, self.animal_name, count))

class Cattle(Animal):

    leg_count = 4
    milk_given = 0

    def give_milk(self, volume):
        self.milk_given += volume
        print("{} {} gave {} liter of milk\n".format(self.animal_type, self.animal_name, volume))

class Sheep(Animal):


    leg_count = 4
    wool_given = 0

    def give_wool(self, weight):
        self.wool_given += weight
        print("{} {} gave {} kg of wool\n".format(self.animal_type, self.animal_name, weight))



def weight_sum():
    weight_sum = 0
    for obj in Animal._instances:
        weight_sum += Animal._instances[obj]
    print(weight_sum)

def heaviest_animal():

    print(max(Animal._instances.items(), key=operator.itemgetter(1))[0])


def main():

    grey = Bird("Grey", "Goose", 5)
    grey.feed()
    grey.lay_eggs(5)

    white = Bird("White", "Goose", 5)
    white.feed()
    white.lay_eggs(7)

    manjka = Cattle("Manjka", "Cow", 800)
    manjka.feed()
    manjka.give_milk(5)

    barashek = Sheep("Barashek", "Sheep", 50)
    barashek.feed()
    barashek.give_wool(4)

    kudrjavij = Sheep("Kudrjavij", "Sheep", 55)
    kudrjavij.feed()
    kudrjavij.give_wool(3)

    koko = Bird("Koko", "Chicken", 2)
    koko.feed()
    koko.lay_eggs(7)

    kukareku = Bird("Kukareku", "Chicken", 2)
    kukareku.feed()
    kukareku.lay_eggs(6)

    roga = Cattle("Roga", "Goat", 40)
    roga.feed()
    roga.give_milk(8)

    kopita = Cattle("Kopita", "Goat", 45)
    kopita.feed()
    kopita.give_milk(6)

    krjakva = Bird("Krjakva", "Duck", 3)
    krjakva.feed()
    krjakva.lay_eggs(8)

    weight_sum()
    heaviest_animal()








if __name__ == '__main__':
    main()
