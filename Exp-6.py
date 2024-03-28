def gcd(a, b):
    """
    Returns the greatest common divisor of a and b using Euclid's algorithm.
    """
    while b != 0:
        a, b = b, a % b
    return a

def find_inverse(a):
    """
    Finds the modular multiplicative inverse of a modulo 26.
    """
    for x in range(1, 26):
        if (a * x) % 26 == 1:
            return x
    return None

def affine_decipher(a, b, ciphertext):
    """
    Decrypts the ciphertext encrypted using the affine Caesar cipher with parameters a and b.
    """
    inverse_a = find_inverse(a)
    if inverse_a is None:
        return "Inverse of 'a' does not exist."

    plaintext = ""
    for char in ciphertext:
        if char.isalpha():  # Process only alphabetical characters
            if char.isupper():  # For uppercase letters
                plaintext += chr(((inverse_a * ((ord(char) - 65) - b)) % 26) + 65)
            elif char.islower():  # For lowercase letters
                plaintext += chr(((inverse_a * ((ord(char) - 97) - b)) % 26) + 97)
        else:
            plaintext += char  # Keep non-alphabetical characters unchanged
    return plaintext

def break_affine_cipher(most_freq, second_most_freq):
    """
    Breaks the affine cipher given the most frequent and second most frequent letters in the ciphertext.
    """
    most_freq_ord = ord(most_freq) - ord('E')
    second_most_freq_ord = ord(second_most_freq) - ord('T')

    a = most_freq_ord * find_inverse(second_most_freq_ord)
    a = a % 26

    b = (ord(most_freq) - ord('E')) * find_inverse(a)
    b = b % 26

    return a, b

# Given information
most_freq_letter = 'B'
second_most_freq_letter = 'U'
ciphertext = "Some ciphertext here..."

# Break the affine cipher
a, b = break_affine_cipher(most_freq_letter, second_most_freq_letter)
print("Deciphering using a =", a, "and b =", b)
decrypted_text = affine_decipher(a, b, ciphertext)
print("Decrypted text:", decrypted_text)
