# bill = input("What is your total bill: ")
# n_o_p = input("Enter the number of person you wanted to divide this bill: ")
# tip = input("Enter the tip you want to apply on your bill (12),(15),(20):  ")
# tip =round((int(bill)*int(tip))/100)
# total_bill =int(bill)+int(tip)
# distribution = round(total_bill/int(n_o_p))
# print(f"Your total bill is Rs.{total_bill}\nEvery pesron have to pay Rs.{distribution}\nThanks for the tip of Rs.{tip}\nThanks for eating !!!")

# Another version

print("Welcome to Tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10,12, or 15? "))
people = int(input("How many people to split the bill? "))
tip_as_percent = tip/100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill/people
final_bill_amount = round(bill_per_person,2)
final_bill_amount = "{:.2f}".format(bill_per_person) # Here : represent the value before decimal end up here and 2f
# represent that we want only 2 values after decimal either we have more than two values after decimal but we want only two
print(f"Each person should have to pay {final_bill_amount}")





# some alphabets to format the value in other data types
# d	for integers
# f	for floating point numbers
# b	for binary numbers
# o	for octal numbers
# x	for octal hexadecimal numbers
# s	for string
# e	for floating point in exponent format

# Source (https://thepythonguru.com/python-string-formatting/)

# ___________________________________________________________________

# Highlight of this session

# Input function
# Type casting
# Format method
# Operators