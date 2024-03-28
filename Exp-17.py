# Initial Permutation (IP) table
initial_permutation_table = [
    57, 49, 41, 33, 25, 17, 9, 1,
    59, 51, 43, 35, 27, 19, 11, 3,
    61, 53, 45, 37, 29, 21, 13, 5,
    63, 55, 47, 39, 31, 23, 15, 7,
    56, 48, 40, 32, 24, 16, 8, 0,
    58, 50, 42, 34, 26, 18, 10, 2,
    60, 52, 44, 36, 28, 20, 12, 4,
    62, 54, 46, 38, 30, 22, 14, 6
]

# Final Permutation (FP) table
final_permutation_table = [
    39, 7, 47, 15, 55, 23, 63, 31,
    38, 6, 46, 14, 54, 22, 62, 30,
    37, 5, 45, 13, 53, 21, 61, 29,
    36, 4, 44, 12, 52, 20, 60, 28,
    35, 3, 43, 11, 51, 19, 59, 27,
    34, 2, 42, 10, 50, 18, 58, 26,
    33, 1, 41, 9, 49, 17, 57, 25,
    32, 0, 40, 8, 48, 16, 56, 24
]

# Key shift schedule for decryption
key_shift_schedule = [
    0, 1, 1, 2, 2, 2, 2, 2,
    1, 2, 2, 2, 2, 2, 2, 1
]

# Function to perform permutation on the input according to the given permutation table
def permute(input_block, permutation_table):
    output_block = [0] * len(permutation_table)
    for i, bit_position in enumerate(permutation_table):
        output_block[i] = input_block[bit_position]
    return output_block

# Function to perform DES decryption
def des_decrypt(ciphertext, keys):
    # Initial permutation
    ciphertext = permute(ciphertext, initial_permutation_table)
    
    # Split the ciphertext into left and right halves
    left_half = ciphertext[:32]
    right_half = ciphertext[32:]

    # 16 rounds of DES
    for i in range(15, -1, -1):  # Reverse order
        # Expand the right half
        expanded_right_half = permute(right_half, expansion_table)
        
        # XOR the expanded right half with the current subkey
        subkey = keys[i]
        xor_result = [((bit1 + bit2) % 2) for bit1, bit2 in zip(expanded_right_half, subkey)]
        
        # Apply S-boxes
        s_box_output = s_box_substitution(xor_result)
        
        # Permute the output of S-boxes
        permuted_s_box_output = permute(s_box_output, permutation_table)
        
        # XOR the permuted output with the left half
        new_right_half = [((bit1 + bit2) % 2) for bit1, bit2 in zip(left_half, permuted_s_box_output)]
        
        # Update left and right halves for the next round
        left_half = right_half
        right_half = new_right_half

        # Apply key shift schedule for decryption
        if i > 0:
            right_half = key_shift(right_half, key_shift_schedule[i])

    # Concatenate the final left and right halves
    output_block = left_half + right_half

    # Final permutation
    plaintext = permute(output_block, final_permutation_table)
    
    return plaintext

def main():
    # Example ciphertext and keys
    ciphertext = [
        0, 0, 1, 0, 0, 1, 0, 1,  # Example ciphertext bits
        1, 0, 0, 0, 1, 0, 1, 1,  # Example ciphertext bits
        # ...
    ]
    keys = [
        # Example keys, each key is a list of 48 bits
        # K1, K2, ..., K16 in reverse order
        [0, 1, 1, 1, 1, 1, 1, 0,  # Example key bits
