import os
import math



def read_file(file_path):
    plaintext = ''
    with open(file_path, 'r') as file:
        plaintext = file.read(-1)
    return plaintext


def save_file(file_path, words):
    f = open(file_path, "w+")
    for i in words:
        f.write(i)
    f.close()


def substitution(plaintext, secret_key, encrypt_decrypt):

    print(plaintext)

    alpha_list_lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
                        'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
                        'w', 'x', 'y', 'z']
    alpha_list_upper = ['A', 'B', 'C', 'D', 'E', 'F',
                        'G', 'H', 'I', 'J', 'K', 'L', 'M',
                        'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
                        'W', 'X', 'Y', 'Z']

    encrypted_text = ''

    for char in plaintext:
        if char in alpha_list_lower:
            index = alpha_list_lower.index(char)
            if encrypt_decrypt == "e":  # Encryption
                encrypted_text += alpha_list_lower[(index + secret_key) % 26]
            elif encrypt_decrypt == "d":  # Decryption
                encrypted_text += alpha_list_lower[(index - secret_key) % 26]
        elif char in alpha_list_upper:
            index = alpha_list_upper.index(char)
            if encrypt_decrypt == "e":  # Encryption
                encrypted_text += alpha_list_upper[(index + secret_key) % 26].upper()
            elif encrypt_decrypt == "d":  # Decryption
                encrypted_text += alpha_list_upper[(index - secret_key) % 26].upper()
        else:
            encrypted_text += char
    if encrypt_decrypt == "e":  # Encryption
        outhpath = "encrypted_substitution_output.txt"
        save_file(outhpath, encrypted_text)
    elif encrypt_decrypt == "d":  # Decryption
        outhpath = "decrypted_substitution_output.txt"
        save_file(outhpath, encrypted_text)


def transposition(plaintext, secret_key, encrypt_decrypt):
    # ENCRYPTION
    if encrypt_decrypt == "e":
        encrypted_cipher = ''

        txt_length = len(plaintext)
        plaintext_lst = list(plaintext)

        key_lst = sorted(list(secret_key))

        col = len(secret_key)
        max_row = int(math.ceil(txt_length / col))

        fill_empty = int((max_row * col) - txt_length)
        plaintext_lst.extend(' ' * fill_empty)

        matrix = []
        for i in range(0, len(plaintext_lst), col):
            matrix += [plaintext_lst[i: i + col]]

        key_index = 0
        for col in range(col):
            curr_index = secret_key.index(key_lst[key_index])
            for row in matrix:
                encrypted_cipher += ''.join([row[curr_index]])
            key_index += 1

        outhpath = "encrypted_transposition_output.txt"
        save_file(outhpath, encrypted_cipher)
        print(encrypted_cipher)

    # DECRYPTION
    elif encrypt_decrypt == "d":
        decrypted_cipher = ""

        k_indx = 0
        plaintext_indx = 0

        plaintext_len = len(plaintext)
        plaintext_lst = list(plaintext)

        col = len(secret_key)
        row = int(math.ceil(plaintext_len / col))

        key_lst = sorted(list(secret_key))

        d_cipher = []
        for r in range(row):
            d_cipher += [[None] * col]

        for c in range(col):
            curr_idx = secret_key.index(key_lst[k_indx])

            for i in range(row):
                d_cipher[i][curr_idx] = plaintext_lst[plaintext_indx]
                plaintext_indx += 1
            k_indx += 1

        decrypted_cipher = ''.join(sum(d_cipher, []))

        outhpath = "decrypted_transposition_output.txt"
        save_file(outhpath, decrypted_cipher)
        print(decrypted_cipher)


print('---------------------------------------------------')
print('1. Encryption\n2. Decryption')

encrypt_decrypt = input('Encryption/Decryption [e/d]: ').lower()
file_name = input('Select a file name: ')
file_path = os.getcwd() + '/' + file_name
plaintext = read_file(file_path)

if encrypt_decrypt == 'e':  # ENCRYPTION
    print('---------------------------------------------------')
    print('1. Substitution\n2. Transposition')
    encryption_method = input('Encryption method [s/t]: ').lower()
    if encryption_method == 's':
        # SUBSTITUTION
        secret_key = int(input('Enter a step: '))
        if secret_key < 256:
            substitution(plaintext, secret_key, encrypt_decrypt)
        else:
            print("The key size should be less than 256")
    elif encryption_method == 't':
        # TRANSPOSITION
        secret_key = input('Enter a key: ')
        transposition(plaintext, secret_key, encrypt_decrypt)
elif encrypt_decrypt == 'd':  # DECRYPTION
    print('---------------------------------------------------')
    print('1. Substitution\n2. Transposition')
    encryption_method = input('Encryption method [s/t]: ').lower()
    if encryption_method == 's':
        # SUBSTITUTION
        secret_key = int(input('Enter a step: '))
        if secret_key < 256:
            substitution(plaintext, secret_key, encrypt_decrypt)
        else:
            print("The key size should be less than 256")
    elif encryption_method == 't':
        # TRANSPOSITION
        secret_key = input('Enter a key: ')
        transposition(plaintext, secret_key, encrypt_decrypt)



