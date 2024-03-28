import string

def generate_cipher_sequence(keyword):
    keyword = keyword.upper()
    cipher_sequence = list(keyword)

    # Add unused letters in normal order
    for letter in string.ascii_uppercase:
        if letter not in cipher_sequence:
            cipher_sequence.append(letter)

    return ''.join(cipher_sequence)

def encrypt(plaintext, cipher_sequence):
    ciphertext = ''
    for char in plaintext:
        if char.isalpha():
            if char.islower():
                index = ord(char) - ord('a')
                ciphertext += cipher_sequence[index].lower()
            else:
                index = ord(char) - ord('A')
                ciphertext += cipher_sequence[index]
        else:
            ciphertext += char
    return ciphertext

def decrypt(ciphertext, cipher_sequence):
    plaintext = ''
    for char in ciphertext:
        if char.isalpha():
            index = cipher_sequence.find(char.upper())
            if char.islower():
                plaintext += chr(index + ord('a'))
            else:
                plaintext += chr(index + ord('A'))
        else:
            plaintext += char
    return plaintext

def main():
    keyword = "CIPHER"
    cipher_sequence = generate_cipher_sequence(keyword)

    plaintext = input("Enter the plaintext: ")
    ciphertext = encrypt(plaintext, cipher_sequence)
    decrypted_text = decrypt(ciphertext, cipher_sequence)

    print("Plaintext:", plaintext)
    print("Ciphertext:", ciphertext)
    print("Decrypted text:", decrypted_text)

if __name__ == "__main__":
    main()
