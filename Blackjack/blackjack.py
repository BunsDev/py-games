from util import deal_card, calculate_score

user_cards = []
computer_cards = []

first_card_user = deal_card()
second_card_user = deal_card()
first_card_computer = deal_card()
second_card_computer = deal_card()

user_cards.append(first_card_user)
user_cards.append(second_card_user)
computer_cards.append(first_card_computer)
computer_cards.append(second_card_computer)

score_player_1 = calculate_score(user_cards)
score_player_2 = calculate_score(computer_cards)
