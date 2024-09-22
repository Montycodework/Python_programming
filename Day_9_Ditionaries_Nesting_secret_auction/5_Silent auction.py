from replit import clear

bidder_name = input("What is your name?\n")
bidder_amount = input("What is the bid amount?\n")

# Adding the input into dictionary
bid_dictionary = {}
def bidding(name, amount):
  bid_dictionary[bidder_name] = bidder_amount
# bidding(name = bidder_name, amount = bidder_amount)
# print(bid_dictionary)
#---------------------------------------------------------

# Highest bid




# Run the input function again and again acording th ask input
again = True
while again:
  ask = input("Type 'y' if any other bidder or 'n' if not...")
  if ask =="y":
    clear()
    bidder_name = input("What is your name?\n")
    bidder_amount = input("What is the bid amount?\n")
    bidding(name = bidder_name, amount = bidder_amount)
  else:
    max_bid(bid_dictionary)
    again = False
    



