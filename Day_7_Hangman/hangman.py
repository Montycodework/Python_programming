# In this game we ll go through 
'''For & while loop , if/ else , lists , strings , range , modules '''
#----------------------------------------------------------------------
import random
stages = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

print(''' _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/ ''')

# Lets understand the steps with flow chart


# To select the random word from list
word_list = ["sonu","monu","monty","shivaye","jonti","hemalta"]
choosen_word = random.choice(word_list)
print(choosen_word) 

# lets check the letter belongs to the random word 
guess = input("Guess a Letter: ").lower()

# for n in choosen_word:
#   if n == guess:
#     print("Yes")
#   else:
#     print("No")  

# Making the choosen_word a list to change it with blanks

choosenword_list =[]

for n in choosen_word:
  choosenword_list += n
# print(choosenword_list)

# Changing the items with blanks

# for n in choosenword_list:    # We can also use _ on place of n and range(len(choosenword_list) on the place of choosenword_list)
blank_list = []
for _ in range(len(choosenword_list)):
  blank_list += "_"
# print(blank_list)  

# now if the guess word is blong to the word then place it at that same place in choosen word:

for position in range(len(choosenword_list)):
  letter = choosenword_list[position]
  if letter == guess:
    blank_list[position] = letter
print(blank_list)    

# guess the letter again for next process and put that on its correct place
# ------------------By for loop --------------------

# for n in range(len(choosenword_list) - 1):
#      guess = input("Guess a Letter: ").lower()
#      for position in range(len(choosenword_list)):
#          letter = choosenword_list[position]
#          if letter == guess:
#             blank_list[position] = letter
#             print(blank_list)    


#  ------------You can use while loop also for this--------------------
# use not  logical operator
s = 0
life = 6
end_of_game = False

while not end_of_game:
  guess = input("Guess a Letter: ").lower()
  for position in range(len(choosenword_list)):
      letter = choosenword_list[position]
      if letter == guess:
          blank_list[position] = letter
          print(blank_list) 

  if guess not in choosenword_list:
    life -= 1
    s += 1
    print(blank_list)
    print(stages[s-1])
    if life == 0:
      end_of_game = True
      print("You Loose") 

  if "_" not in blank_list:
    end_of_game = True
    print("You won")
  
  
   


