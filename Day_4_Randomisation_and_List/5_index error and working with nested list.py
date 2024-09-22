states_of_india = ["Andhra Pradesh","Arunachal Pradesh ","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana",
                   "Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Madhya Pradesh",
                   "Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim",
                   "Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal",
                   "Andaman and Nicobar Islands","Chandigarh","Dadra and Nagar Haveli","Daman and Diu",
                   "Lakshadweep","National Capital Territory of Delhi","Puducherry"]

# print(states_of_india[50]) # Out of range error in a list
number_of_states = len(states_of_india)
# print(states_of_india[number_of_states]) #  we get a same error because len gives us actual number of states but
# when work with index you get number_of_states-1 brcause +ve index starts from 0 and ends at number of items-1 .

print(states_of_india[number_of_states - 1])



# Nested list

fruits=['apples','oranges','bananas','mangoes','grapes','strawberry','potato','brinjal','carrot','tomato','colyflower']
# in this list fruits and vegis both are present how can we split them easily


fruits=['apples','oranges','bananas','mangoes','grapes','strawberry']
Vegis = ['potato','brinjal','carrot','tomato','colyflower']
nested_list = [fruits,Vegis]
print(nested_list[1][1])
# List in a list is called nested list.

# print(nested_list)


# _________________________________________________________________________________
# Highlights of this session

# nested list (Joining)
# technique to use index number on diff places
# list methods