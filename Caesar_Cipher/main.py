import util
import art

print(art.logo)

should_continue = True
while should_continue:

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")

    if direction != 'encode' and direction != 'decode':
        print('Invalid input')
        exit()

    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    shift = shift % 26

    util.caesar(text, shift, direction)

    ask_continue_using = input('Would you like to start again? Type "yes" to continue, else type "no"\n')

    if ask_continue_using == 'no':
        print('Goodbye')
        should_continue = False
