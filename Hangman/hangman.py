import random
import util

random_word = random.choice(util.word_list)

end_of_game = False
display = []
word_length = len(random_word)

for _ in range(word_length):
    display += "_"
print(f'The word you need to guess is {word_length} letters long:\n{display}')

while not end_of_game:
    guessed_letter = input('Guess a letter:\n').lower()

    for index in range(word_length):
        letter = random_word[index]
        if letter == guessed_letter:
            display[index] = guessed_letter

    if "_" not in display:
        end_of_game = True
        print("You win")
    else:
        print(display)

print(f'The word was {random_word}')
