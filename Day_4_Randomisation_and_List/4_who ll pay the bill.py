import random

names = input("Give me the name of everybody sits here\n")
names1 = names.split(", ") # To split the items comes from input and put it inside a list as a individual items so we can apply a len function on it. 

# x = len(names1) 
# bill_payer = random.randint(0,x-1) # Len function gives us the actual number of items in list but for indexing we need item - 1 thats why we r using x-1 here.
# person_who_pay_bill = names1[bill_payer]

# instead of doing above you can manage with this one



# new technique
person_who_pay_bill = random.choice(names1)  # random.choice() is the function to choose the item from list randomly

print(f"The person who pay the bill is {person_who_pay_bill}")


# _____________________________________________________________________________
# Highlights of this session

# random
# input
# split function
# random.choice function
# f-string