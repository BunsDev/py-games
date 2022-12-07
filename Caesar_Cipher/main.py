import util
import art

print(art.logo)

while True:

    continue_using = input('If you want to continue using the program, press "yes", else press "no"\n')

    if continue_using == 'yes':

        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")

        if direction != 'encode' and direction != 'decode':
            print('Invalid input')
            exit()

        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))

        shift = shift % 26

        util.caesar(text, shift, direction)
    elif continue_using == 'no':
        print('Goodbye')
        exit()
