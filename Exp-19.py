from Crypto.Cipher import DES3
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes

def encrypt_cbc_3des(plaintext, key, iv):
    cipher = DES3.new(key, DES3.MODE_CBC, iv)
    padded_plaintext = pad(plaintext.encode(), DES3.block_size)
    ciphertext = cipher.encrypt(padded_plaintext)
    return ciphertext

def main():
    # Example plaintext, key, and initialization vector (IV)
    plaintext = "Hello, world!"
    key = get_random_bytes(24)  # 24 bytes = 192 bits for 3DES
    iv = get_random_bytes(8)     # 8 bytes = 64 bits for IV

    # Encrypt the plaintext using 3DES in CBC mode
    ciphertext = encrypt_cbc_3des(plaintext, key, iv)
    print("Ciphertext:", ciphertext)

if __name__ == "__main__":
    main()
