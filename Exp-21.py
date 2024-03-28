from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

# AES block size in bytes
BLOCK_SIZE = 16

# Padding function to ensure plaintext length is a multiple of block size
def pad_plaintext(plaintext):
    padding_length = BLOCK_SIZE - (len(plaintext) % BLOCK_SIZE)
    return plaintext + bytes([padding_length] * padding_length)

# Unpadding function to remove padding from plaintext
def unpad_plaintext(plaintext):
    padding_length = plaintext[-1]
    return plaintext[:-padding_length]

# ECB encryption function
def encrypt_ecb(plaintext, key):
    cipher = AES.new(key, AES.MODE_ECB)
    padded_plaintext = pad_plaintext(plaintext)
    ciphertext = cipher.encrypt(padded_plaintext)
    return ciphertext

# ECB decryption function
def decrypt_ecb(ciphertext, key):
    cipher = AES.new(key, AES.MODE_ECB)
    decrypted_padded_plaintext = cipher.decrypt(ciphertext)
    plaintext = unpad_plaintext(decrypted_padded_plaintext)
    return plaintext

# CBC encryption function
def encrypt_cbc(plaintext, key, iv):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    padded_plaintext = pad_plaintext(plaintext)
    ciphertext = cipher.encrypt(padded_plaintext)
    return ciphertext

# CBC decryption function
def decrypt_cbc(ciphertext, key, iv):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted_padded_plaintext = cipher.decrypt(ciphertext)
    plaintext = unpad_plaintext(decrypted_padded_plaintext)
    return plaintext

# CFB encryption function
def encrypt_cfb(plaintext, key, iv):
    cipher = AES.new(key, AES.MODE_CFB, iv, segment_size=BLOCK_SIZE * 8)
    ciphertext = cipher.encrypt(plaintext)
    return ciphertext

# CFB decryption function
def decrypt_cfb(ciphertext, key, iv):
    cipher = AES.new(key, AES.MODE_CFB, iv, segment_size=BLOCK_SIZE * 8)
    plaintext = cipher.decrypt(ciphertext)
    return plaintext

def main():
    # Generate random key and IV
    key = get_random_bytes(BLOCK_SIZE)
    iv = get_random_bytes(BLOCK_SIZE)

    # Example plaintext
    plaintext = b'This is a secret message.'

    # Encrypt and decrypt using ECB mode
    print("ECB Mode:")
    ciphertext_ecb = encrypt_ecb(plaintext, key)
    decrypted_text_ecb = decrypt_ecb(ciphertext_ecb, key)
    print("Plaintext:", plaintext)
    print("Ciphertext (ECB):", ciphertext_ecb)
    print("Decrypted Text (ECB):", decrypted_text_ecb)

    # Encrypt and decrypt using CBC mode
    print("\nCBC Mode:")
    ciphertext_cbc = encrypt_cbc(plaintext, key, iv)
    decrypted_text_cbc = decrypt_cbc(ciphertext_cbc, key, iv)
    print("Plaintext:", plaintext)
    print("Ciphertext (CBC):", ciphertext_cbc)
    print("Decrypted Text (CBC):", decrypted_text_cbc)

    # Encrypt and decrypt using CFB mode
    print("\nCFB Mode:")
    ciphertext_cfb = encrypt_cfb(plaintext, key, iv)
    decrypted_text_cfb = decrypt_cfb(ciphertext_cfb, key, iv)
    print("Plaintext:", plaintext)
    print("Ciphertext (CFB):", ciphertext_cfb)
    print("Decrypted Text (CFB):", decrypted_text_cfb)

if __name__ == "__main__":
    main()
