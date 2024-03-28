class PolyalphabeticSubstitutionCipher:
    def __init__(self, key):
        self.key = key

    def encrypt(self, plaintext):
        plaintext = plaintext.upper()
        ciphertext = ''
        key_index = 0
        for char in plaintext:
            if char.isalpha():
                shift = ord(self.key[key_index % len(self.key)].upper()) - ord('A')
                encrypted_char = self.shift_char(char, shift)
                ciphertext += encrypted_char
                key_index += 1
            else:
                ciphertext += char
        return ciphertext

    def decrypt(self, ciphertext):
        ciphertext = ciphertext.upper()
        plaintext = ''
        key_index = 0
        for char in ciphertext:
            if char.isalpha():
                shift = ord(self.key[key_index % len(self.key)].upper()) - ord('A')
                decrypted_char = self.shift_char(char, -shift)
                plaintext += decrypted_char
                key_index += 1
            else:
                plaintext += char
        return plaintext

    def shift_char(self, char, shift):
        shifted_value = ord(char) + shift
        if char.isupper():
            if shifted_value > ord('Z'):
                shifted_value -= 26
            elif shifted_value < ord('A'):
                shifted_value += 26
        elif char.islower():
            if shifted_value > ord('z'):
                shifted_value -= 26
            elif shifted_value < ord('a'):
                shifted_value += 26
        return chr(shifted_value)


# Example usage:
if __name__ == "__main__":
    key = "KEY"
    plaintext = "Hello World!"
    cipher = PolyalphabeticSubstitutionCipher(key)
    encrypted_text = cipher.encrypt(plaintext)
    decrypted_text = cipher.decrypt(encrypted_text)
    print("Plaintext:", plaintext)
    print("Encrypted:", encrypted_text)
    print("Decrypted:", decrypted_text)
