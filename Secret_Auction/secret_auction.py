from art import logo
from util import clear

stop_bidding = False
max_bid = 0
remember_bidder = ""

while not stop_bidding:
    print(logo)

    bidder_name = input("What is your name?\n")
    bid_value = float(input("What is your bid?\n"))

    bidders = {
        bidder_name: bid_value
    }

    other_bidders = input("Are there other bidders? Type 'yes' or 'no'\n")
    if other_bidders == 'yes':
        clear()
    elif other_bidders == 'no':
        stop_bidding = True
        clear()

    if bid_value > max_bid:
        max_bid = bid_value
        remember_bidder = bidder_name

print(f"The highest bidder was {remember_bidder} with bid: ${max_bid}")
