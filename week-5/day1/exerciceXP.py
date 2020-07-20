#exercice1

class Cat:
    species = 'mammal'
    def __init__(self, name, age):
        self.name = name
        self.age = age

max_age = 0
def oldest_cat(max_age):
    for current_cat in my_cats:
        if current_cat > max_age:
            max_age = current_cat
            print(max_age)

my_cats=[Cat("nouou",5) ,Cat("fourour",8),Cat("tttt",4)]


















#Exercice2

class Dog:
    def __init__(self,name,heigthDog):
        self.name= name
        self.heigthDog= heigthDog



    def talk (self):
        print(f"{self.name} says wouaff wouaff")

    def jump (self):
        print("the jumps is heigth",self.heigthDog*2)

davids_dog= Dog("Rex",50 )
davids_dog.talk()
davids_dog.jump()



# OOP INTERMEDIARE





#exercice 3

class song:
    def __init__(self,lyric):
        self.lyric= lyric

    def sing_me_a_song(self):
        for line in self.lyric:
            for word in line.split(" "):
                print(word)

happy_birthday= song(["happy birthday to you","how old are you"])
happy_birthday.sing_me_a_song()
#
# #lyric =[
#     "happy birthday to you",
#     "you belong to a zoo",
#     "you look like a monkey",
#     "you djdjekj in one too"]



class Circle:
    color = "red"

class NewCircle(Circle):
    color = "blue"

nc = NewCircle
print(nc.color)


class Circle:
    def __init__(self, diameter):
      self.diameter = diameter

    def grow(self, factor=2):
        """grows the circle's diameter by factor"""
        self.diameter = self.diameter * factor

class NewCircle(Circle):
    def grow(self, factor=2):
        """grows the area by factor..."""
        self.diameter = (self.diameter * factor * 2)

nc = NewCircle(1)
print(nc.diameter)
nc.grow()
print(nc.diameter)






