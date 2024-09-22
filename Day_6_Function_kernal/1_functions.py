# print("Hello") #These round brackets are the proof that print() is the function something
# comes in these round brackets is the actual item on which we are running that function.
# len("Hello") # len is also a function to find out the length of that char in any string
# char_length = len("Hello")
# print(char_length)


# How to make a function

# def my_function(): 
#   print("Hello")
#   print("Bye")
# my_function() # Here we are calling our function by its name and inside that function has been executes line by line 

# go to reborgs world on google an do some excercises


# Indentation

# def my_function():
#     print("Hello") # Here before print function we are having 4 spaces indentation.
# print("Hello world")    # This print function is not the park og my_function because this print function don't have indentation before it .

# sky = "clear"
sky = "cloudy"

def my_function():
  if sky == "clear":
  elif sky == "cloudy":
    print("blue")
    print("grey")
  print("Hello")
print("World")  # This world comes first because we are calling this print function seperatly before my_function.     
my_function()