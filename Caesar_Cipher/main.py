import util

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")

if direction != 'encode' and direction != 'decode':
    print('Invalid input')
    exit()

text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

if direction == 'encode':
    util.encrypt(text, shift)
elif direction == 'decode':
    util.decrypt(text, shift)
