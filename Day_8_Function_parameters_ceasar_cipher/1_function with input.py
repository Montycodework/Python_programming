# functions with inputs

# Basic
def greet(something): # Something is the place where the user input store and convyed in function.
    # Do this task with something
    # Then Do this task
    # Finally do this 
    print(f"Hello {something} !!")
greet("string")    


# With name
def greet(name): 
    print(f"Hello {name} !!")
greet("Monty")


# With input 
User = input("Enter the name: ")
def greet(name): 
    print(f"Hello {name} !!")
greet(User) 

