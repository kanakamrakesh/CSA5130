def affine_caesar_cipher(a, b, plaintext):
    """
    Encrypts the plaintext using the affine Caesar cipher with parameters a and b.
    """
    ciphertext = ""
    for char in plaintext:
        if char.isalpha():  
            if char.isupper():  
                ciphertext += chr(((a * (ord(char) - 65)) + b) % 26 + 65)
            elif char.islower():  
                ciphertext += chr(((a * (ord(char) - 97)) + b) % 26 + 97)
        else:
            ciphertext += char  
    return ciphertext
def affine_decipher(a, b, ciphertext):
    """
    Decrypts the ciphertext encrypted using the affine Caesar cipher with parameters a and b.
    """
    inverse_a = 0
    for i in range(26):
        if (a * i) % 26 == 1:
            inverse_a = i
            break
    plaintext = ""
    for char in ciphertext:
        if char.isalpha():  
            if char.isupper():
                plaintext += chr(((inverse_a * ((ord(char) - 65) - b)) % 26) + 65)
            elif char.islower():  
                plaintext += chr(((inverse_a * ((ord(char) - 97) - b)) % 26) + 97)
        else:
            plaintext += char  
    return plaintext
a = 3
b = 7
plaintext = "Hello, World!"
encrypted_text = affine_caesar_cipher(a, b, plaintext)
print("Encrypted:", encrypted_text)
decrypted_text = affine_decipher(a, b, encrypted_text)
print("Decrypted:", decrypted_text)
