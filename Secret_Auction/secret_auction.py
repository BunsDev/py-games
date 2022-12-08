from art import logo
from util import clear, find_highest_bidder

stop_bidding = False
bidders = {}

while not stop_bidding:
    print(logo)

    bidder_name = input("What is your name?\n")
    bid_value = float(input("What is your bid?\n"))

    bidders[bidder_name] = bid_value

    other_bidders = input("Are there any other bidders? Type 'yes' or 'no'.\n")
    if other_bidders == 'yes':
        clear()
    elif other_bidders == 'no':
        stop_bidding = True
        clear()

data = find_highest_bidder(bidders)

print(f"The highest bidder was {data[0]} with bid: ${data[1]}")
