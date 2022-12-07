import util
import random

end_of_game = False
chosen_word = random.choice(util.word_list)
word_length = len(chosen_word)

lives = 6

print(f'Pssst, the solution is {chosen_word}.')
print(f"Welcome to Hangman! You have {lives} lives total. Be careful")

display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:

    if lives == 0:
        print('You lose')
        exit()

    guess = input("Guess a letter: \n").lower()

    if guess in display:
        if lives == 0:
            print('You lose')
            exit()
        else:
            lives -= 1
            print(f'Your lives have been decreased by 1, now you have {lives}')
            continue

    if guess not in chosen_word:
        if lives == 0:
            print('You lose')
            exit()
        else:
            lives -= 1
            print(f'Your lives have been decreased by 1, now you have {lives}')
            continue

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You win.")
