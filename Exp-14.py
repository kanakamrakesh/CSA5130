def vigenere_encrypt(plaintext, key):
    ciphertext = ''
    for i in range(len(plaintext)):
        if plaintext[i].isalpha():
            shift = key[i % len(key)]
            encrypted_char = chr(((ord(plaintext[i]) - ord('a') + shift) % 26) + ord('a'))
            ciphertext += encrypted_char
        else:
            ciphertext += plaintext[i]
    return ciphertext

def vigenere_decrypt(ciphertext, key):
    plaintext = ''
    for i in range(len(ciphertext)):
        if ciphertext[i].isalpha():
            shift = key[i % len(key)]
            decrypted_char = chr(((ord(ciphertext[i]) - ord('a') - shift) % 26) + ord('a'))
            plaintext += decrypted_char
        else:
            plaintext += ciphertext[i]
    return plaintext

def main():
    plaintext = "sendmoremoney"
    key = [9, 0, 1, 7, 23, 15, 21, 14, 11, 11, 2, 8, 9]

    # Part (a): Encrypt the plaintext
    ciphertext = vigenere_encrypt(plaintext, key)
    print("Encrypted ciphertext:", ciphertext)

    # Part (b): Decrypt the ciphertext to 'cash not needed'
    target_plaintext = "cashnotneeded"
    target_ciphertext = vigenere_encrypt(target_plaintext, key)
    print("Target ciphertext:", target_ciphertext)

    # Find the key to decrypt the ciphertext to the target plaintext
    found_key = [(ord(target_ciphertext[i]) - ord(ciphertext[i])) % 26 for i in range(len(target_ciphertext))]
    print("Found key:", found_key)

    # Decrypt the ciphertext using the found key
    decrypted_text = vigenere_decrypt(ciphertext, found_key)
    print("Decrypted text:", decrypted_text)

if __name__ == "__main__":
    main()
