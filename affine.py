def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def mod_inverse(a, m):
    for i in range(1, m):
        if (a * i) % m == 1:
            return i
    return None

def affine_encrypt(text, a, b):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            if char.islower():
                encrypted_text += chr(((a * (ord(char) - ord('a')) + b) % 26) + ord('a'))
            else:
                encrypted_text += chr(((a * (ord(char) - ord('A')) + b) % 26) + ord('A'))
        else:
            encrypted_text += char
    return encrypted_text

# Input
text = input("Enter the text to be encrypted: ")
a = int(input("Enter the value of 'a' (must be coprime with 26): "))
b = int(input("Enter the value of 'b': "))

# Check if 'a' is coprime with 26
if gcd(a, 26) != 1:
    print("Error: 'a' is not coprime with 26. Please choose another value for 'a'.")
else:
    # Encrypt the text
    encrypted_text = affine_encrypt(text, a, b)
    print("Encrypted text:", encrypted_text)
