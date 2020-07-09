


dict = {
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "city": "New york" ,
 'best_friend': {
    'name': 'Felix',
    'age': 4.5
  },
  'favorite_foods': ['steaks', 'sausages', 'shawarma']
}

dict['name']="nathaniel"
dict['weigth']= 87
print(dict)


print(dict['best_friend']['name'],dict['favorite_foods'])






print( "the age of kelly is :" ,dict["city"])
keysToRemove = ["name", "salary"]

for key in keysToRemove:
    del dict[key]

print(dict)


names= [ "jon" , "nath" ,"tsivia", "alon"]


shirts = [
  {
    'name': 'Awesome T-shirt 3000',
    'size': 'S',
    'price': 20
  },
  {
    'name': 'Awesome T-shirt 3500',
    'size': 'M',
    'price': 25
  },
  {
    'name': 'Awesome T-shirt 5000',
    'size': 'L',
    'price': 30
  },
]
shirts[0]['price']=12
if 'price' in shirts:
    print("OUIIIIIIIIIII")

for shirt in shirts :
    print(shirt['price'])
for name_shirt in shirts:
    print("the name of this t-shirt is :",name_shirt['name'])

for size in shirts:
    print(size['size'])

print(dict.keys())

sampleDict = {
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "city": "New york"

}
keysToRemove = ["name", "salary"]
for key in keysToRemove :
    del sampleDict[key]
    print(sampleDict)

my_number = "nathaniel"
my_list = []

for num in my_number:
    my_list.append(num)
print(my_list)

my_sister= "emmanuelle"


my_books = {
  "title": "Harry Potter",
  "author": "JK Rowling",
}

for x, y, in my_books.items():
    print("the ", x , " is ", y )






