



def calcul(x,y):
    return x + y ,x - y

print(calcul(30,76))


def myinfo(**kwargs):
    for key in kwargs.keys():
        key_str = " ".join(key.split("_"))
        print(f"Your {key_str} is {kwargs[key]}")
    return kwargs
print(myinfo(first_name="Yair", middle_name="George", last_name="Hochner",
             age=28, profession="Developer"))
d = dict(first_name="Yair", middle_name="George", last_name="Hochner",
             age=28, profession="Developer")

x= "helloword"
print(f"{x} "*5)


age = input("How old are you? ")
print(age)
print("You are {} years old".format(age))
