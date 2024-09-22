#############################   SCOPE    ############################

# enemies = 1 # Global scope

# def increase_enemies():
#   enemies = 2 # Local scope
#   print(f"Your enemies are {enemies}")

# increase_enemies()
# print(f"Your enemies are {enemies}") 

# # Local SCOPE

# def drinking_potion():
#   potion_strength = 2 # Local scope only works inside the function
#   print(potion_strength)

# drinking_potion()  
# print(potion_strength) # This print function can't access that potion_strength because that variable is inside the function and that is called local scope.


# Global SCOPE

# potion_strength = 2 # Global scope 

# def drinking_potion():
#   print(potion_strength) # works inside the function

# drinking_potion()
# print(potion_strength)  # Here the gobal scope is works inside and outside of the function


# Global scope another version

# potion_count = 2 # Global scope 

# def drinking_potion():
#   potion_strength = 2 # Local scope
#   print(potion_count) # works inside the function
#   print(potion_strength)
# drinking_potion()
# print(potion_strength) # It is a Local scope its doesn't work outside function
# print(potion_count)


# potion_count = 2
# def game():
#   def drinking_potion(): # Local scope (you can call this function only inside the game() function if you called it without indent then u got an error.)
#     potion_strength = 2
#     print(potion_strength)
#     print(potion_count)
# # drinking_potion() # You need to indent inside the game() function to call this function.
#   drinking_potion()
# print(potion_count)  


# There is no block scope 

# if
# while
# for
# These statements are not consider any variable as Local scope 
# Wheather the variable is indented or not it called as global scope inside the whole function
# game_life = 3
# game_player = ["Vegita","Goku","pinaka"]
# if game_life < 5:
#    new_player = game_player[0]

# print(new_player) # This new player is created inside the if function but printed without indent out the statement 
# print(game_life)



# But these statements are inside any def functions then variable inside that function considered as local scope 
# game_life = 3
# def game():
#   game_player = ["Vegita","Goku","pinaka"]
#   if game_life < 5:
#     new_player = game_player[0]

# # print(new_player) # This new player is created inside the if function and now its inside the game function so it called as a local scope and now can't printed without indent .  
#   print(new_player)
# print(game_life)

# Modifying a global scope

# enemies = 1 # Global scope

# def increase_enemies():
#   global enemies # do not try to modify a gobal scope lots of dev not recommend it .
#   enemies += 1
#   print(f"Your enemies are {enemies}")

# increase_enemies()
# print(f"Your enemies are {enemies}") 

# So how can you make the logic without modifying the global scope
enemies = 1 # Global scope

def increase_enemies():
  # global enemies # instead of doing this!!
  # enemies += 1 # just place it into return statement
  print(f"Your enemies are {enemies}")
  return enemies + 1 # Now you get the value by adding the value of 1 in your enemies when you call the function 

increase_enemies()
print(f"Your enemies are {enemies}")