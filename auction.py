

import os
print('''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
''')

bids={}
bidding_finished=False

def find_highest_bidder(bidding_record):
  highest_bid=0
  winner=""
  for bidder in bidding_record:
    bid_amount=bidding_record[bidder]
    if bid_amount>highest_bid:
      highest_bid=bid_amount
      winner=bidder
  print(f"The winner is {winner} with a bid of {highest_bid}")

while not bidding_finished:
  name=input("Enter the name of the bidder: ")
  bid_price=int(input("Enter the bid price: "))
  
  bids[name]=bid_price
  should_continue=input("Are there any other bidders? Type 'yes' or 'no':")
  if should_continue=="no":
    bidding_finished=True
    find_highest_bidder(bids)
  elif should_continue=="yes":
    def clear_screen():
      os.system('cls')
    clear_screen()
  else:
    print("Wrong Input")


  



 
 


