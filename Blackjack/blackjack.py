from util import *

final_score_player = 0
final_score_computer = 0

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
        score_player = 0
        is_not_over = False
    elif has_blackjack_computer:
        score_computer = 0
        print('The computer has blackjack and wins!')
        is_not_over = False

    if has_busted_user:
        print(f'The user has busted! The score is {score_player}')
        is_not_over = False

    elif has_busted_computer:
        print(f'The user has busted! The score is {final_score_player} with cards {user_deck}')
        is_not_over = False

        print(f'The user has busted! The score is {final_score_player} with cards {user_deck}')

    print(
        f'The user has score of {score_player} with deck {user_deck}\nThe computer has score of {score_computer} with deck {computer_deck}')
    choice = input('To draw another card type "y", else type "n", for the game to end\n')

    if choice == 'y':
        add_new_card(user_deck)
        final_score_player = calculate_score(user_deck)
        check_if_busted = check_for_busted(final_score_player)
        if check_if_busted == True:
            print(f'The user has busted! The score is {final_score_player} with cards {user_deck}')
            is_not_over = False
    else:
        if score_computer < 17:
            add_new_card(computer_deck)
            final_score_computer = calculate_score(computer_deck)
            check_if_busted_comp = check_for_busted(final_score_computer)
            if check_if_busted_comp == True:
                print(f"The computer has busted! The score is {final_score_computer} with cards: {computer_deck}")
                is_not_over = False
        elif 17 <= score_computer <= 21:
            compare(final_score_player, final_score_computer)


        else:
            print(f"The computer has busted! The score is {calculate_score(computer_deck)} with cards: {computer_deck}")
