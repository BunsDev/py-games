alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']


def encrypt(plain_text, shift_amount):
    message_encrypt = ''
    for i in range(len(plain_text)):
        current_char = plain_text[i]
        index = alphabet.index(current_char)
        index += shift_amount
        new_char = alphabet[index]
        message_encrypt += new_char
    print('The encrypted message is: ' + message_encrypt)


def decrypt(plain_text, shift_amount):
    message_decrypt = ''
    for i in range(len(plain_text)):
        current_char = plain_text[i]
        index = alphabet.index(current_char)
        index -= shift_amount
        new_char = alphabet[index]
        message_decrypt += new_char
    print('The decrypted message is: ' + message_decrypt)
