fruits = ["item1","items2"]       # list with string items
fruits = [1,2,3,4]                # List with integers
fruits = [1.2,22.34,40.01]        # list with float values
fruits = [True,False]             # List with boolean values
fruits = ["item1",1,22.34,True]   # list with mixed values


# a single variable with more that one values inside it with square brackets

states_of_india = ["Andhra Pradesh","Arunachal Pradesh ","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana",
                   "Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Madhya Pradesh",
                   "Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan",
                   "Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal",
                   "Andaman and Nicobar Islands","Chandigarh","Dadra and Nagar Haveli","Daman and Diu",
                   "Lakshadweep","National Capital Territory of Delhi","Puducherry"]

print(states_of_india[6]) # to get the particular state name by their index number starting from (0 to number of items-1) if u are having 3 items in your list so your index ll be 0,1,2 
# positive index start from left to right 
# every item has its own index number in list 
# Why we are starting from zero : because after  =  there is an offset which create that item on zero position

print(states_of_india[-5])
# Negative index start from right to left and it is also having the starting value as -1 so it started from -1 to number of item

states_of_india.append("Jaatland") # this append function add this value in the last of this list
print(states_of_india)



# any() function to check the data inside list
if any("Goa" in word for word in states_of_india):
    print("Goa is there")


# for other list function go to python documentation

# _______________________________________________________________________

# Highlights of this session

# list
# list methods
# How to copy the list from google
# python documentation