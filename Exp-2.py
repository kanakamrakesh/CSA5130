import random

class MonoalphabeticSubstitutionCipher:
    def __init__(self):
        self.plaintext_alphabet = 'abcdefghijklmnopqrstuvwxyz'
        self.ciphertext_alphabet = self.generate_random_ciphertext_alphabet()

    def generate_random_ciphertext_alphabet(self):
        alphabet = list(self.plaintext_alphabet)
        random.shuffle(alphabet)
        return ''.join(alphabet)

    def encrypt(self, plaintext):
        ciphertext = ''
        for char in plaintext:
            if char.lower() in self.plaintext_alphabet:
                index = self.plaintext_alphabet.index(char.lower())
                if char.isupper():
                    ciphertext += self.ciphertext_alphabet[index].upper()
                else:
                    ciphertext += self.ciphertext_alphabet[index]
            else:
                ciphertext += char
        return ciphertext

    def decrypt(self, ciphertext):
        plaintext = ''
        for char in ciphertext:
            if char.lower() in self.ciphertext_alphabet:
                index = self.ciphertext_alphabet.index(char.lower())
                if char.isupper():
                    plaintext += self.plaintext_alphabet[index].upper()
                else:
                    plaintext += self.plaintext_alphabet[index]
            else:
                plaintext += char
        return plaintext

# Example usage:
if __name__ == "__main__":
    cipher = MonoalphabeticSubstitutionCipher()
    plaintext = "hello world"
    encrypted_text = cipher.encrypt(plaintext)
    decrypted_text = cipher.decrypt(encrypted_text)
    print("Plaintext:", plaintext)
    print("Encrypted:", encrypted_text)
    print("Decrypted:", decrypted_text)
