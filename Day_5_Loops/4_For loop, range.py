# For loop with range
# for number in range(a , b)
# print(number)

# example: 

# for number in range(1 , 10):
# in this you got 1,2,3,4,5,6,7,8,9 only you didnt get the 10 because range start from first argument and end just before the last it cannot consider the last number.
# for example if your mom says that you need to play in the range of your house walls so you have to play in the range of tha walls not on tha walls you dont need to touch the wall to find out the range of your playing area.
  # print(number)

for number in range(1 , 10 , 2): # If you want the numbers which having a difference of 2 number between them similarly just put that number on the place of 2 if you want some other kind of difference 
# This 2 in the range is called as STEP size of range
  print(number)


# Sum of first 100 natural numbers using range function with for Loop

sum = 0
for number in range(1 , 101):
  sum += number
print(sum)  

