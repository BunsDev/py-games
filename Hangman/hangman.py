import random
import util

random_word = random.choice(util.word_list)

guessed_letter = input('Guess a letter:\n ').lower()

for letter in random_word:
    if letter == guessed_letter:
        print('match')
    else:
        print('wrong')

print(f'The word was {random_word}')
