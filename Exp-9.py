def create_key(key):
    key = key.upper().replace(" ", "")
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"  # Note: 'J' is removed from the alphabet
    key_set = set()
    key_matrix = []

    for letter in key:
        if letter not in key_set and letter in alphabet:
            key_set.add(letter)
            key_matrix.append(letter)

    for letter in alphabet:
        if letter not in key_set:
            key_matrix.append(letter)

    return key_matrix


def decrypt(message, key):
    decrypted_message = ""
    key_matrix = create_key(key)

    for i in range(0, len(message), 2):
        if message[i] == " ":  # Ignore spaces
            decrypted_message += " "
            continue

        row1, col1 = divmod(key_matrix.index(message[i]), 5)
        row2, col2 = divmod(key_matrix.index(message[i + 1]), 5)

        if row1 == row2:
            decrypted_message += key_matrix[row1 * 5 + (col1 - 1) % 5] + key_matrix[row2 * 5 + (col2 - 1) % 5]
        elif col1 == col2:
            decrypted_message += key_matrix[((row1 - 1) % 5) * 5 + col1] + key_matrix[((row2 - 1) % 5) * 5 + col2]
        else:
            decrypted_message += key_matrix[row1 * 5 + col2] + key_matrix[row2 * 5 + col1]

    return decrypted_message


def main():
    message = "KXJEY UREBE ZWEHE WRYTU HEYFS KREHE GOYFI WTTTU OLKSY CAJPO BOTEI ZONTX BYBNT GONEY CUZWR GDSON SXBOU YWRHE BAAHY USEDQ"
    key = "PT109A"

    decrypted_message = decrypt(message.replace(" ", ""), key)
    print("Decrypted message:", decrypted_message)


if __name__ == "__main__":
    main()
