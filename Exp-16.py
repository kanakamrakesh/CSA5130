import itertools
import collections

# Function to decrypt ciphertext using a specific letter mapping
def decrypt(ciphertext, mapping):
    decrypted_text = ''
    for char in ciphertext:
        if char.isalpha():
            decrypted_char = mapping.get(char.lower(), char)
            decrypted_text += decrypted_char.upper() if char.isupper() else decrypted_char
        else:
            decrypted_text += char
    return decrypted_text

# Function to calculate letter frequencies in text
def calculate_frequencies(text):
    letter_count = collections.Counter(char for char in text if char.isalpha())
    total_letters = sum(letter_count.values())
    frequencies = {char: count / total_letters for char, count in letter_count.items()}
    return frequencies

# Function to generate all possible letter mappings
def generate_mappings():
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    mappings = itertools.permutations(alphabet)
    return [''.join(mapping) for mapping in mappings]

# Function to perform letter frequency attack on monoalphabetic substitution cipher
def letter_frequency_attack(ciphertext, top_n=10):
    possible_plaintexts = []

    mappings = generate_mappings()

    # Try all possible letter mappings
    for mapping in mappings:
        decrypted_text = decrypt(ciphertext, dict(zip(mapping, 'abcdefghijklmnopqrstuvwxyz')))
        frequencies = calculate_frequencies(decrypted_text)
        possible_plaintexts.append((decrypted_text, frequencies))

    # Sort possible plaintexts based on frequency of 'e' (most common letter in English)
    sorted_plaintexts = sorted(possible_plaintexts, key=lambda x: x[1].get('e', 0), reverse=True)

    return sorted_plaintexts[:top_n]

def main():
    ciphertext = "Gwc uivioml bw nqvl bpm zqopb apqnb."
    top_n = 10

    possible_plaintexts = letter_frequency_attack(ciphertext, top_n)

    print(f"Top {top_n} possible plaintexts:")
    for i, (plaintext, frequencies) in enumerate(possible_plaintexts, start=1):
        print(f"\nPlaintext {i}:")
        print(plaintext)
        print("Letter Frequencies:")
        print(frequencies)

if __name__ == "__main__":
    main()
