import random
import util

random_word = random.choice(util.word_list)

guessed_letter = input('Guess a letter:\n ').lower()

display = []
word_length = len(random_word)

for _ in range(word_length):
    display += "_"
print(display)


for index in range(word_length):
    if random_word[index] == guessed_letter:
        display[index] = guessed_letter

print(f'The word was {random_word}')
