# Initial permutation (IP) table
initial_permutation_table = [
    58, 50, 42, 34, 26, 18, 10, 2,
    60, 52, 44, 36, 28, 20, 12, 4,
    62, 54, 46, 38, 30, 22, 14, 6,
    64, 56, 48, 40, 32, 24, 16, 8,
    57, 49, 41, 33, 25, 17, 9, 1,
    59, 51, 43, 35, 27, 19, 11, 3,
    61, 53, 45, 37, 29, 21, 13, 5,
    63, 55, 47, 39, 31, 23, 15, 7
]

# Permuted choice 1 (PC1) table for key
permuted_choice_1_table = [
    57, 49, 41, 33, 25, 17, 9,
    1, 58, 50, 42, 34, 26, 18,
    10, 2, 59, 51, 43, 35, 27,
    19, 11, 3, 60, 52, 44, 36,
    63, 55, 47, 39, 31, 23, 15,
    7, 62, 54, 46, 38, 30, 22,
    14, 6, 61, 53, 45, 37, 29,
    21, 13, 5, 28, 20, 12, 4
]

# Permuted choice 2 (PC2) table for key
permuted_choice_2_table = [
    14, 17, 11, 24, 1, 5, 3, 28,
    15, 6, 21, 10, 23, 19, 12, 4,
    26, 8, 16, 7, 27, 20, 13, 2,
    41, 52, 31, 37, 47, 55, 30, 40,
    51, 45, 33, 48, 44, 49, 39, 56,
    34, 53, 46, 42, 50, 36, 29, 32
]

# Key shift schedule
key_shift_schedule = [
    1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1
]

# Function to perform permutation on the input according to the given permutation table
def permute(input_block, permutation_table):
    return [input_block[i - 1] for i in permutation_table]

# Function to generate 16 subkeys for DES encryption
def generate_subkeys(key):
    # Perform permutation choice 1 (PC1) on the key
    pc1_key = permute(key, permuted_choice_1_table)

    # Split the key into two halves
    left_half = pc1_key[:28]
    right_half = pc1_key[28:]

    subkeys = []

    # Generate 16 subkeys
    for i in range(16):
        # Apply key shift schedule
        for _ in range(key_shift_schedule[i]):
            left_half.append(left_half.pop(0))
            right_half.append(right_half.pop(0))

        # Combine the halves
        combined_half = left_half + right_half

        # Perform permutation choice 2 (PC2) on the combined halves
        subkey = permute(combined_half, permuted_choice_2_table)

        subkeys.append(subkey)

    return subkeys

def main():
    # Example initial key (64 bits)
    initial_key = [
        0, 0, 0, 0, 0, 0, 0, 0,  # Example key bits (64 bits)
        # ...
    ]

    # Generate subkeys
    subkeys = generate_subkeys(initial_key)

    # Print the generated subkeys
    print("Generated Subkeys:")
    for i, subkey in enumerate(subkeys, start=1):
        print(f"Subkey {i}: {subkey}")

if __name__ == "__main__":
    main()
