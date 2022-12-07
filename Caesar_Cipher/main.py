import util

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")

if direction != 'encode' and direction != 'decode':
    print('Invalid input')
    exit()

text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def encrypt(plain_text, shift_amount):
    message = ''
    for i in range(len(plain_text)):
        current_char = plain_text[i]
        index = util.alphabet.index(current_char)
        index += shift_amount
        new_char = util.alphabet[index]
        message += new_char
    print(message)


encrypt(plain_text=text, shift_amount=shift)
