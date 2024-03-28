def decrypt_simple_substitution(ciphertext):
    # Define the mapping of characters in the cipher to plaintext
    mapping = {
        '†': 'a', '‡': 'b', '*': 'c', ';': 'd', '(': 'e',
        ')': 'f', '4': 'g', '8': 'h', '6': 'i', '5': 'j',
        '3': 'k', '0': 'l', ':': 'm', '2': 'n', '—': 'o',
        ']': 'p', '1': 'q', '9': 'r', ']:': 's', '?': 't',
        '¶': 'u', '5;': 'v', '28': 'w', '48': 'x', '81': 'y',
        '96': 'z', '34': ' '
    }

    plaintext = ''
    i = 0
    while i < len(ciphertext):
        # If there are special cases like '†9' or ']8*', combine them first
        if i + 2 < len(ciphertext) and ciphertext[i:i + 2] in mapping:
            plaintext += mapping[ciphertext[i:i + 2]]
            i += 2
        # If not special case, look for single characters in mapping
        elif ciphertext[i] in mapping:
            plaintext += mapping[ciphertext[i]]
            i += 1
        else:
            # If character is not in mapping, just add it as it is
            plaintext += ciphertext[i]
            i += 1

    return plaintext

ciphertext = "53‡‡†305))6*;4826)4‡.)4‡);806*;48†8¶60))85;;]8*;:‡*8†83 (88)5*†;46(;88*96*?;8)*‡(;485);5*†2:*‡(;4956*2(5*—4)8¶8* ;4069285);)6†8)4‡‡;1(‡9;48081;8:8‡1;48†85;4)485†528806*81 (‡9;48;(88;4(‡?34;48)4‡;161;:188;‡?"
plaintext = decrypt_simple_substitution(ciphertext)
print("Decrypted plaintext:")
print(plaintext)
