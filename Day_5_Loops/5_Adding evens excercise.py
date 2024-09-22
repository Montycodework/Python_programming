
# sum of the only even numbers between 1 - 100
evens = 0
for number in range(2 , 101 , 2):   # Here 2 is the diff between two numbers within the range
  evens += number
print(evens)  

#----------------------------------------------------
# another version
even = 0
for number in range(1 , 101):
  if number % 2 == 0:
    even +=number
print(even)    