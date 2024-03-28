import collections

# Function to decrypt ciphertext using additive cipher with a specific shift
def decrypt(ciphertext, shift):
    decrypted_text = ''
    for char in ciphertext:
        if char.isalpha():
            decrypted_char = chr(((ord(char) - ord('a') - shift) % 26) + ord('a'))
            decrypted_text += decrypted_char
        else:
            decrypted_text += char
    return decrypted_text

# Function to calculate letter frequencies in text
def calculate_frequencies(text):
    letter_count = collections.Counter(char for char in text if char.isalpha())
    total_letters = sum(letter_count.values())
    frequencies = {char: count / total_letters for char, count in letter_count.items()}
    return frequencies

# Function to perform letter frequency attack on additive cipher
def letter_frequency_attack(ciphertext, top_n=10):
    possible_plaintexts = []

    # Try all possible shifts (1 to 25)
    for shift in range(1, 26):
        decrypted_text = decrypt(ciphertext, shift)
        frequencies = calculate_frequencies(decrypted_text)
        possible_plaintexts.append((decrypted_text, frequencies))

    # Sort possible plaintexts based on frequency of 'e' (most common letter in English)
    sorted_plaintexts = sorted(possible_plaintexts, key=lambda x: x[1].get('e', 0), reverse=True)

    return sorted_plaintexts[:top_n]

def main():
    ciphertext = "Hw uif xpsme xbt tvdi boe spttf, zpv epo'u ep tpnfuijoh ju."
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
