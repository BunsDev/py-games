import util

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")

if direction != 'encode' and 'decode':
    print('Invalid input')
    exit()

text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def encrypt(text_param, shift_param):
    message = ''
    for index in range(len(text_param)):
        current_char = text_param[index]
        index = util.alphabet.index(current_char)
        index += shift_param
        new_char = util.alphabet[index]
        message += new_char
    print(message)


encrypt(text, shift)
