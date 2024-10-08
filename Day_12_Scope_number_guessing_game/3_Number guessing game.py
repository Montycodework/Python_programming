import random
from art import logo
print(logo)
############### My version ##################3

# print("I'm thinking the number between 1 to 100")

# # number guessed by computer
# number_guesssed = random.randint(1, 100)

# # Level of dificulty to attempt the guess
# level = input("Choose the dificulty: Type 'easy' or 'hard' ")

# # Guess function of user
# def guesses():
#   if user_number == number_guesssed:
#     print(f"You win the number is: {number_guesssed}")
#     is_continue = True
#   elif user_number <= number_guesssed:
#     print(f"{user_number} is Too low")
#   else:
#     print(f"{user_number} is Too high")

# is_continue = False
# while not is_continue:
#   if number_guessed
#   is_continue = True

# # User input start
# if level == "easy":
#   print("You have 10 attempt to guess the numbers")
#   for _ in range(10):
#     user_number = int(input("Guess the number: "))
#     guesses()
#   print("Attempts over now")  
# else:
#   print("You have 5 attempts to guess the number")
#   for _ in range(5):
#     user_number = int(input("Guess the number: "))
#     guesses()
#   print("Attempts over now")  

################### Computer verson ################

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

#Function to check user's guess against actual answer.
def check_answer(guess, answer, turns):
  """checks answer against guess. Returns the number of turns remaining."""
  if guess > answer:
    print("Too high.")
    return turns - 1
  elif guess < answer:
    print("Too low.")
    return turns - 1
  else:
    print(f"You got it! The answer was {answer}.")

#Make function to set difficulty.
def set_difficulty():
  level = input("Choose a difficulty. Type 'easy' or 'hard': ")
  if level == "easy":
    return EASY_LEVEL_TURNS
  else:
    return HARD_LEVEL_TURNS

def game():
  print(logo)
  #Choosing a random number between 1 and 100.
  print("Welcome to the Number Guessing Game!")
  print("I'm thinking of a number between 1 and 100.")
  answer = random.randint(1, 100)
  print(f"Pssst, the correct answer is {answer}") 

  turns = set_difficulty()
  #Repeat the guessing functionality if they get it wrong.
  guess = 0
  while guess != answer:
    print(f"You have {turns} attempts remaining to guess the number.")

    #Let the user guess a number.
    guess = int(input("Make a guess: "))

    #Track the number of turns and reduce by 1 if they get it wrong.
    turns = check_answer(guess, answer, turns)
    if turns == 0:
      print("You've run out of guesses, you lose.")
      return
    elif guess != answer:
      print("Guess again.")


game()