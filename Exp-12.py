import numpy as np

# Function to encrypt the plaintext using the Hill cipher with the provided key
def hill_encrypt(plaintext, key):
    # Convert plaintext to numerical representation (a=0, b=1, ..., z=25)
    numerical_plaintext = [ord(char) - ord('a') for char in plaintext if char.isalpha()]

    # Pad the plaintext if necessary
    if len(numerical_plaintext) % 2 != 0:
        numerical_plaintext.append(ord('x') - ord('a'))  # Adding 'x' to make pairs

    # Split the plaintext into pairs for the Hill cipher
    pairs = [(numerical_plaintext[i], numerical_plaintext[i + 1]) for i in range(0, len(numerical_plaintext), 2)]

    # Convert key to numpy array
    key_matrix = np.array(key)

    # Encrypt the pairs using the Hill cipher
    encrypted_pairs = []
    for pair in pairs:
        numerical_cipher = np.dot(key_matrix, np.array(pair)) % 26
        encrypted_pairs.append(numerical_cipher)

    # Convert numerical ciphertext back to letters
    ciphertext = ''.join([chr(pair[0] + ord('a')) + chr(pair[1] + ord('a')) for pair in encrypted_pairs])

    return ciphertext

# Function to decrypt the ciphertext using the Hill cipher with the provided key
def hill_decrypt(ciphertext, key):
    # Convert ciphertext to numerical representation (a=0, b=1, ..., z=25)
    numerical_ciphertext = [ord(char) - ord('a') for char in ciphertext if char.isalpha()]

    # Convert key to numpy array and calculate its inverse
    key_matrix = np.array(key)
    key_inverse = np.linalg.inv(key_matrix)
    key_inverse = np.round((key_inverse * np.linalg.det(key_matrix)) % 26).astype(int)

    # Decrypt the ciphertext using the Hill cipher
    decrypted_pairs = []
    for pair in numerical_ciphertext:
        numerical_plain = np.dot(key_inverse, np.array(pair)) % 26
        decrypted_pairs.append(numerical_plain)

    # Convert numerical plaintext back to letters
    plaintext = ''.join([chr(pair + ord('a')) for pair in decrypted_pairs])

    return plaintext

def main():
    # Key matrix
    key = [[9, 4], [5, 7]]

    # Plaintext message
    plaintext = "meetmeattheusualplaceattenratherthaneightoclock"

    # Encrypt the plaintext
    ciphertext = hill_encrypt(plaintext, key)
    print("Encrypted message:", ciphertext)

    # Decrypt the ciphertext
    decrypted_plaintext = hill_decrypt(ciphertext, key)
    print("Decrypted message:", decrypted_plaintext)

if __name__ == "__main__":
    main()
