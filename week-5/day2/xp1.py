class Dog():
    # Initializer / Instance Attributes
    def __init__(self, name_of_the_dog, race):
        print("A new dog has been initialized !")
        print("His name is", name_of_the_dog, "and is race is ", race)
        self.name = name_of_the_dog
        self.race = race

    def bark(self):
         print("{}   barks ! WAF".format(self.name))




my_dog = Dog("rocky", "workshire")
my_dog.bark()

my_dog1 = Dog ("marciano","bulldog")
my_dog1bark()

