# class1 = [150,154,153,152,156,155,157,158,159] # list of a class students height in cm
# print(sum(class1)) # to sum up the integers in the list
# print(len(class1)) # to print the number of items in the list

# but you need to find out another method to find out the average height of the class1
# You are not allowed to use sum, len in this excercise its a challange.

student_height = input("Enter the height of students one by one\n")
height = student_height.split()

# # For making the input items store into a list and make them integers
for n in range(0, len(height)):
  height[n] = int(height[n])
# print(height)

# Sum of items in the list
total_height = 0

for x in height:
  total_height += x # agar aap list ki actual value of use krna chahte ho calculations me to for ke baad wala x,y ya jo bhi aapne likha he vo use karo
# print(total_height)   

# number of items in the list

number_of_students = 0

for student in height:
  number_of_students += 1 # agar aap sirf number of items nikalna chahte ho to  for ke baad ka jo bhi likha he use use mat karo calculations me.
# print(number_of_students)  

average_height = round(total_height/number_of_students)
print(average_height)


# -----------------------------------Short trick----------------------------------------------

# student_height = input("Enter the height of students one by one\n")
# height = student_height.split()

# for n in range(0, len(height)):
#   height[n] = int(height[n])

# total_height = sum(height)
# number_of_students = len(height)
# average_height = round(total_height/number_of_students)
# print(average_height)



# ___________________________________________________________________________

# Hightlights of this session

# sum() method
# len() method
# split() method
# for loop
# range function
# operators