import random
import art


def print_logo():
    print(art.logo)


cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def deal_card():
    return random.choice(cards)


def add_new_card(deck):
    card = random.choice(cards)
    deck.append(card)


def deal_cards():
    deck = []
    first_card = deal_card()
    second_card = deal_card()
    deck.append(first_card)
    deck.append(second_card)
    return deck


def check_for_blackjack(score):
    if score == 21:
        return True
    return False


def calculate_score(deck):
    sum_score = sum(deck)

    # 0 will represent blackjack
    if sum_score == 21:
        return 0
    # There is a case where the player can get two aces. In this case The dealer will remove one ace and replace it with 1
    elif sum_score > 21:
        sum_score -= 10

    return sum(deck)


def check_for_busted(score):
    if score > 21:
        return True
    return False
