# Randomisation (Unpridctibility of some values in our code )

# Deterministic : A machine perform repeated action in fully pridictive way (randomly)

# Khan academy video (psuedo number generator) to lear a littlebit more about pseudo random numbers 

# Python also created some random module on Ask python website

# import random # This is the python module we using for randomisation 

# random_integer = random.randint(1 , 10) # random.randint(starting value, end value) so we can get the random number between start value and end value.
# print(random_integer)


# But what is module?
# Ans. Actually Some complicated tasks have long code and very difficult to understand so this codes are divided into some parts called module so every one can use that part of this code by their require uses.

# for ex - A car has lots of things inside and outside of it so a single man can't manage and do that things in  a car so the works are divided into different parts such as chassis, tyres,interior,engine etc these parts are called modules. 

# import my_module # This is the file we created with main.py and importing it into main.py

# print(my_module.pi) # This is how you need to call that value from module(my_module)



#----------------------------------------------------------------------------------------------------
# random float values

import random

# random_float = random.random() # To get the random float values between 0 and 1 and they are having lots of numbers after decimal
# print(random_float)

# random_float = random.random(0 , 5) # Type error random() never takes arguments and here we are apssing two aguments 0 and 5.
# print(random_float)

random_float = random.random() * 5 # multiply by 5 so u get the values from 0 to 5
print(random_float)


love_score = random.randint(1 , 100)
print(f"Your love score is {love_score}")

