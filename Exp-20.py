def simulate_error_transmission(ciphertext, error_block_index):
    # Simulate an error in the transmitted ciphertext block
    ciphertext_with_error = list(ciphertext)
    ciphertext_with_error[error_block_index] ^= 1  # Flip a bit to simulate an error
    return bytes(ciphertext_with_error)

def main():
    # Example ciphertext blocks (in bytes)
    ciphertext_blocks = [
        b'encrypted_block_1',
        b'encrypted_block_2',
        b'encrypted_block_3',
        b'encrypted_block_4'
    ]

    # Simulate an error in the transmitted ciphertext block C1
    error_block_index = 0
    ciphertext_with_error = simulate_error_transmission(ciphertext_blocks[error_block_index], error_block_index)

    # Print the original and corrupted ciphertext blocks
    print("Original Ciphertext Blocks:")
    for i, block in enumerate(ciphertext_blocks):
        print(f"C{i+1}: {block}")

    print("\nCorrupted Ciphertext Blocks:")
    for i, block in enumerate(ciphertext_blocks):
        if i == error_block_index:
            print(f"C{i+1} (with error): {ciphertext_with_error}")
        else:
            print(f"C{i+1}: {block}")

if __name__ == "__main__":
    main()
