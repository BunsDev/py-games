import random
import util

end_of_game = False
chosen_word = random.choice(util.word_list)
word_length = len(chosen_word)

lives = 6

display = []
for _ in range(word_length):
    display += "_"

print('The word is ' + chosen_word)
print(f'You have {lives} lives total. Be careful')

while not end_of_game:
    guess = input("Guess a letter: \n").lower()

    if guess in display:
        lives -= 1
        print('You already tried this letter, try something new. Subtracting 1 live')
        print(util.stages[lives])
        continue

    if lives == 0:
        end_of_game = True
        print("You lose.")

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        lives -= 1
        print('Incorrect guess. Subtracting 1 live')
        if lives == 0:
            end_of_game = True
            print("You lose.")

    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You win.")

    print(util.stages[lives])

print(f'The word was: {chosen_word}')
