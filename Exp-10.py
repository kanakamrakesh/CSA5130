def create_playfair_matrix(key):
    key = key.replace(" ", "").upper().replace("J", "I")
    key_set = set()
    playfair_matrix = [['' for _ in range(5)] for _ in range(5)]

    row, col = 0, 0
    for char in key + "ABCDEFGHIKLMNOPQRSTUVWXYZ":
        if char not in key_set:
            playfair_matrix[row][col] = char
            key_set.add(char)
            col += 1
            if col == 5:
                col = 0
                row += 1
    return playfair_matrix

def find_position(matrix, char):
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == char:
                return i, j

def encrypt(plaintext, matrix):
    plaintext = plaintext.upper().replace("J", "I").replace(" ", "")
    pairs = [(plaintext[i], plaintext[i+1]) if i != len(plaintext)-1 else (plaintext[i], 'X') for i in range(0, len(plaintext), 2)]

    ciphertext = ''
    for pair in pairs:
        char1, char2 = pair
        row1, col1 = find_position(matrix, char1)
        row2, col2 = find_position(matrix, char2)

        if row1 == row2:
            ciphertext += matrix[row1][(col1 + 1) % 5] + matrix[row2][(col2 + 1) % 5]
        elif col1 == col2:
            ciphertext += matrix[(row1 + 1) % 5][col1] + matrix[(row2 + 1) % 5][col2]
        else:
            ciphertext += matrix[row1][col2] + matrix[row2][col1]

    return ciphertext

def main():
    key = "MFHIJKUNOPQZVWXYELARGDSTBC"
    plaintext = "Must see you over Cadogan West. Coming at once."
    
    playfair_matrix = create_playfair_matrix(key)
    ciphertext = encrypt(plaintext, playfair_matrix)

    print("Encrypted Message:", ciphertext)

if __name__ == "__main__":
    main()
