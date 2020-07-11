# Exercice 1

my_fav_numbers = [ 1 , 18 , 26 , 32 , 260]
my_fav_numbers.extend([55 , 33])
print(my_fav_numbers)

my_fav_numbers.pop(-1)
print(my_fav_numbers)

friend_fav_numbers= [ 2.23 , 34 , 45 , 54, 26]
set(friend_fav_numbers)
print(set (friend_fav_numbers))

our_favorite_numbers = friend_fav_numbers + my_fav_numbers

print(set(our_favorite_numbers))

#exercice 2

#my_fav_numbers1=( 12, 23, 26, 35 ,45)
#my_fav_numbers1.extend(30, 34)
#print(my_fav_numbers1)

# error "tuple" object has no atribute "extend"
#friend_fav_numbers1= (13, 23, 35, 56, 45)
#our_favorite_numbers1 = friend_fav_numbers1 + my_fav_numbers1
#print (set(our_favorite_numbers1))
#error


# exercice3

number = 4.45
print(float(number))
print(int(number))

list_num =[]
i= float
for i in range (0,5) : # The range gave you number of probabilily

    list_num.append(i)
    print(list_num)

# exercice 4

for i  in range ( 1,21):
    print(i)

# ecercice 5

#user = input( "what do you want to add ? if nothing tape /finish\ ")
#while  user!= "finish":
    print ("you will add this topping to your pizza")
#else :
    print("thank you")

# Exercice6

# a fimily of 5 members : 2 parents , 3 childrens ( 17 y , 12 y , 2 y)

list_age=[]
def number_family:
    input(int(f"you are {num} member's family , enter the {num} age ")



number_family(4)

