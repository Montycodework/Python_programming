# Unlimited arguments

# *args
# def unl(*args): # Tum jitni marzi argument pass karo vo unl wale braket me aake jma hote rhenge aur ek tuple create ho
#     # jyega fir forrl loop usko loop me chla ke n se itreate krke print kar dega
#     for n in args:
#         print(n)
# add(1,2,3,4,5,6,7,8,9)   #jitni chahe arguments pass karo

# ________________________________________________________________________________

# def add(*args):
#     print(args[0]) # For checking the actual arguments pass by the user
#     sum = 0
#     for n in args:
#         sum += n
#     return sum

# print(add(1,2,3,4,5,6,7,8,9)) # iska ans 45 milega


# Many keyworded arguments
# **kwargs

# def calculate(n,**kwargs): #jese uper tuple banra he yha dict ban jyegi
#     print(kwargs)
#     for key, value in kwargs.item():
#         # print(key)
#         # print(value)
#        n += kwargs["add"]
#        n += kwargs["multiply"]
#     print(n)
# calculate(2, add = 3, multiply = 5)

# **kwargs ko aur sahi se smjhna he to jab hum tkinter me label lga rhe the to usme kitne sare keyword ke sath arguments
# pass kar rhe the to vo sab **kwargs ki vja se hi tha kyuki def label(**kwargs) use karke bna hoga label function


# calculate(add=3, multiply=5) # Dict ke according 'add' key he aur 3 value
# _____________________________________________

class Car:
    def __init__(self,**kw):
        self.make = kw["make"]
        self.model = kw["model"]

my_car = Car(make = "Nisaan", model = "GT-R") # Isme khali ek likhenge to erorr ayega
print(my_car.make) # You ll get the nissan
print(my_car.model) # You ll gget GT-R

class Car:
    def __init__(self,**kw):
        self.make = kw.get("make")
        self.model = kw.get("model")

my_car = Car(make = "Nisaan") # Isme khali ek likhenge to erorr nhi ayega kyuki kw.get() likha he vo jo nhi jyega use none kardega
print(my_car.make) # You ll get the nissan
# print(my_car.model) # You ll get nothing