from util import *

print_logo()
user_deck = deal_cards()
computer_deck = deal_cards()

score_player = calculate_score(user_deck)
score_computer = calculate_score(computer_deck)

has_blackjack_user = check_for_blackjack(score_player)
has_blackjack_computer = check_for_blackjack(score_computer)
has_busted_user = check_for_busted(score_player)
has_busted_computer = check_for_busted(score_computer)

if has_blackjack_user:
    print('The user has blackjack and wins!')
elif has_blackjack_computer:
    print('The computer has blackjack and wins!')

if has_busted_user:
    print(f'The user has busted! The score is {score_player}')
elif has_busted_computer:
    print(f'The computer has busted! The score is {score_computer}')

print(f'Your score is {score_player}.')
choice = input('To draw another card type "y", else type "n", for the game to end')

if choice == 'y':
    # implement an add new card function
    new_card = deal_card()
