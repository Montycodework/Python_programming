from art import logo
print(logo)


def add(n1, n2):
  return n1 + n2

def sub(n1, n2):
  return n1 - n2 

def mul(n1, n2):
  return n1 * n2 

def div(n1, n2):
  return n1 / n2 

Operations = {
  "+": add, # yha add name ka function humne dictionary me hi bitha dia baki bhi niche ese hi kardie
  "-": sub,
  "*": mul,
  "/": div,  
}

# first_number = int(input("Enter your First number:\n")) 
# for n in Operations:
#   print(n)
# operation_symbol = input("Pick an operation from the above:  ")
# second_number = int(input("Enter your Second number:\n"))
# def answer(symbol):
#   for n in Operations:
#     if symbol == n: # ME galat kar rha tha 
#       return Operations[n] 
# print(answer(symbol = operation_symbol))      

# calculation_function = Operations[operation_symbol] # Yha calculation_function name ka variable bna ke humne Operations name ki dictionaryme se ek operation_symbol ke according function call kar lia 
# answer = calculation_function(first_number, second_number) # answer me humne pehla aur dossra number call  krke function chla dia calculation_function me jo aya he

# print(f"{first_number} {operation_symbol} {second_number} = {answer}")

# Diff between print and return

# operation_symbol = input("Pick an operation from the above:  ")
# third_number = int(input("Enter your third number:\n"))

# calculation_function = Operations[operation_symbol]
# second_answer = calculation_function(first_answer, third_number) # Last answer aur third number pass kar rhe he taki pichle answer me ye number se calculation ho ske

# print(f"{first_answer} {operation_symbol} {third_number} = {second_answer}")


# doing the task with while loop -----------------------
def calculator():
  first_number = float(input("Enter your First number:\n")) 
  for n in Operations:
    print(n)  
  should_continue = True

  while should_continue:
    operation_symbol = input("Pick an operation:  ")
    second_number = float(input("What's the next number:\n"))
    calculation_function = Operations[operation_symbol]
    answer = calculation_function(first_number, second_number)

    print(f"{first_number} {operation_symbol} {second_number} = {answer}")

    if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to exit: ") == "y":
      first_number = answer
    else:
      should_continue = False
      calculator()
  
calculator() # This is called a recursive a function

# when we are trying to enter a float value code crashes so you need to change number input to float now go to the number input (line no 53 & 60) and change them from int to float.