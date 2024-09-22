# Copying the content from previous one

student_height = input("Enter the height of students one by one\n")
height = student_height.split()

# # For making the input items store into a list and make them integers
for n in range(0, len(height)):
  height[n] = int(height[n])
print(height)  


highest_height = 0
for h in height: # yaha actually ho kya rha he ki h height name ki list me
  # gya pehla item uthaya aur ake check kia ki kya highest height > h se bada
  # he to pehla item to bada hi hoga generally to vo element usne higest score
  # ko dedia if ke baad wali command se fir vo dobara gya height name ki list me
  # next item uthaya aur fir agya higest height se compare karne ab agar h jo item
  # utha ke laya he highest score se jyada hua to highest height ko dedega verna next
  # item lake fir compare karega ese karte karte highest height ke pass sbse bada item
  # hi reh jyega aur hum usko print,krke maze lenge hogya gya solve......!!!!!!
  if h > highest_height:
    highest_height = h
print(f"The highest person in this list is: {highest_height}")    
