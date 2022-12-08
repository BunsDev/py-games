from util import *

print_logo()
user_deck = deal_cards()
computer_deck = deal_cards()

is_not_over = True
while is_not_over:
    score_player = calculate_score(user_deck)
    score_computer = calculate_score(computer_deck)

    has_blackjack_user = check_for_blackjack(score_player)
    has_blackjack_computer = check_for_blackjack(score_computer)
    has_busted_user = check_for_busted(score_player)
    has_busted_computer = check_for_busted(score_computer)

    if has_blackjack_user:
        print('The user has blackjack and wins!')
        is_not_over = False
    elif has_blackjack_computer:
        print('The computer has blackjack and wins!')
        is_not_over = False

    if has_busted_user:
        print(f'The user has busted! The score is {score_player}')
        is_not_over = False

    elif has_busted_computer:
        print(f'The computer has busted! The score is {score_computer}')
        is_not_over = False

    print(f'Your cards are {user_deck} and you have score {score_player}')

    choice = input('To draw another card type "y", else type "n", for the game to end\n')

    if choice == 'y':
        add_new_card(user_deck)
        new_score_player = calculate_score(user_deck)
        check_if_busted = check_for_busted(new_score_player)
        if check_if_busted == True:
            print(f'The user has busted! The score is {new_score_player}')
            is_not_over = False
    else:
        print_logo()
        exit()
