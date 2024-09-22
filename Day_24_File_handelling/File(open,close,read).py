# file = open("mytext.txt") # inside brackets its a external file
# contents = file.read() # Here i am assigning the opened file to a variable.
# print(contents)
# file.close() # If you are opening a file then u must close that file in the end.
# other wise computer ll close it by itself after sometime. (jese chrome me tabs jitni jyada khhuli hongi ram aur
# internet uthna hi slow hota jyega isse accha he khud hi file ko close kardo  )



# Doosra tareeka file ko open karne ka

# with open("mytext.txt") as file:      Ye by default read only mode hota he
#     contents = file.read()
#     print(contents)

# File ko write (Changes) karne ke liye

# with open("mytext.txt" ,mode = "w") as file:
#     file.write("Ye he nyi line") # ab ye line mytext.txt me jake pehle wali line ko replace kardegi
#     print(file)

# Agar pehle wali line na kaar ke ek nayi line jodni ho

# with open("mytext.txt" ,mode = "a") as file:
#     file.write("\nYe he nyi line") # ab ye line mytext.txt me jake pehle wali line ke sath add ho jyegi.



# Koi nayi file yahi se banani ho

with open("mytext2.txt",mode="w") as file: # Ye nayi file sirf write mode me hi banti he.
    file.write("mytext2.txt")