from art import logo
from util import clear, find_highest_bidder

stop_bidding = False
bidders = {}

while not stop_bidding:
    print(logo)

    bidder_name = input("What is your name?:\n")
    bid_value = input("What is your bid?: $\n")

    try:
        bid_value = float(bid_value)
    except ValueError:
        print('The provided bid is not a number!')
        exit()

    bidders[bidder_name] = bid_value

    other_bidders = input("Are there any other bidders? Type 'yes' or 'no'.\n")
    if other_bidders == 'yes':
        clear()
    elif other_bidders == 'no':
        stop_bidding = True
        clear()

data = find_highest_bidder(bidders)
name = data[0]
bid = float(data[1])

print(f"The highest bidder was {name} with bid: ${bid}")
