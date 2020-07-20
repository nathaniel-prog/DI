

def favorite_book(title):
    print(f'my favorite book is {title}')


favorite_book("harrypotter")

#exercice 3

def make_shirt(size='L', text='i love python'):
    print(f'the new shirt is size:{size} and has the message: {text}')

#make_shirt('m', 'hello world') # positional arguments
#make_shirt() # default arguments
#make_shirt(text='hello Nathaniel', size='xl') #keyword arguments

make_shirt()
#make_shirt(text="j'ai compris ", size="xxxxl")

make_shirt(text="ilive in france", )

word= 0
def mouzar_word(sentences):
    for word in sentences.split():
        if len(word) > 6 and "e" and "a" not in word:
          print(word)
        else:
            print("no words matches")

mouzar_word(" salut ment ")

#Exercises XP
#exercice 4  Day 4 - Functions


list_magicien = [ "harry potter", "david copper", "whatever" ]

def show_magicien():
    for magicien in list_magicien:
        print(magicien)

show_magicien()

def make_great(list_magicien):
    for i in range(len(list_magicien)):
          list_magicien[i]+=" the Great"


make_great(list_magicien)

show_magicien()

#exercice 5

def describe_city(name_of_city,country="USA"):
    print(f"{name_of_city} is in {country}")

describe_city("london", )


#exercice 6



def get_age(year_of_birth=1988,month_of_birth=9,day_of_birth=11):#default value
    current_month=7
    current_year=2020
    current_day= 20
    if current_month < month_of_birth  :
        return (abs( year_of_birth - current_year)) - 1
    elif current_month ==current_month and current_day< day_of_birth:
        return(abs( year_of_birth - current_year)) - 1
    else:
        return (current_year-year_of_birth)

my_age= get_age(1957,4,14)
print(my_age)



def can_retire():
    gender=input("are you a male or a femalle:")
    print(gender)
    date_of_birth= get_age(input("what is your date of birth"))
    print(date_of_birth)


can_retire()












#get_age(year=2020, month=7 , day= 19)

#def can_retire(gender,date_of_birth):









