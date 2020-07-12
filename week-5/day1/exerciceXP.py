#exercice1

class Cat:
    species = 'mammal'
    def __init__(self, name, age):
        self.name = name
        self.age = age


#Exercice2

class dog:
    def __int__(self,name,heigthDog):
        self.name= name
        self.heigthDog= heigthDog


    def talk (self):
        print("wouaff wouaff")


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

lyric =[
    "happy birthday to you",
    "you belong to a zoo",
    "you look like a monkey",
    "you djdjekj in one too"
]

for line in lyric:
    for word in line.split(" "):
        print(word)







