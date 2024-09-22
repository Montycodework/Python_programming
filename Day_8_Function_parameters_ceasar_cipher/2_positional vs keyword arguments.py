# Function with more than 1 input 

def greet(name, location):
  print(f"My name is {name}")
  print(f"I live in {location}")

greet("Monty","Delhi")  

# let just switch the given data

greet("Delhi","Monty") # jo pehle data hoga co def greet ke baad pehle argument me hi jyega chahe kuch bhi ho aur
# doosra doosre me isko bolte he position of data and argument.


# with 3 Arguments
def my_function(a, b, c):
  print(f"This is {a}")
  print(f"This is {b}")
  print(f"This is {c}")

my_function(10,20,30)  
# yha bhi jo pehle jyega vo pehle me ghus jyega doosra doosre compile
def my_function(a, b, c):
  print(f"This is {c}")
  print(f"This is {a}")
  print(f"This is {b}")
# Isse bachne ke lie arguments ko pass krte smye hi sara baat bta do

my_function(a=10, b=20, c=30) # ab isko kisi bhi trha likh lo jo tha ye vahi rhega aur function ke
# under bhi jake change nhi hoga cahe vha bhi kisi bhi order me likha ho.

def my_function(a, b, c):
  print(f"This is {a}")
  print(f"This is {c}")
  print(f"This is {b}")
my_function(a=10, c=30, b=20) # yha bhi result same 