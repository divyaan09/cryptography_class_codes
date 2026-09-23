# Vigenere Cipher Program

def clean(text):
    return "".join(ch for ch in text if ch.isalpha())

def repeat_key(text, key):
    key = key.upper()
    return "".join(key[i % len(key)] for i in range(len(text)))

def to_nums(text):
    return [ord(ch.upper()) - ord('A') for ch in text]

def vigenere_encrypt(text, key):
    plain = clean(text).upper()
    full_key = repeat_key(plain, key)

    p_nums = to_nums(plain)
    k_nums = to_nums(full_key)
    c_nums = [(p + k) % 26 for p, k in zip(p_nums, k_nums)]

    cipher = "".join(chr(c + ord('A')) for c in c_nums)
    return plain, full_key, cipher, p_nums, k_nums, c_nums

def vigenere_decrypt(cipher, key):
    cipher = clean(cipher).upper()
    full_key = repeat_key(cipher, key)

    c_nums = to_nums(cipher)
    k_nums = to_nums(full_key)
    p_nums = [(c - k) % 26 for c, k in zip(c_nums, k_nums)]

    plain = "".join(chr(p + ord('A')) for p in p_nums)
    return cipher, full_key, plain, c_nums, k_nums, p_nums

# ---- Main ----
mode = input("Encrypt or Decrypt? (e/d): ")
key = input("Enter keyword: ")

if mode == 'e':
    text = input("Enter plaintext: ")
    plain, full_key, cipher, p_nums, k_nums, c_nums = vigenere_encrypt(text, key)

    print("\nPlaintext:      ", " ".join(plain))
    print("Plaintext (num):", p_nums)
    print("Key:            ", " ".join(full_key))
    print("Key (num):      ", k_nums)
    print("Ciphertext:     ", " ".join(cipher))
    print("Ciphertext (num):", c_nums)
    print("\nFinal Ciphertext:", cipher)

else:
    text = input("Enter ciphertext: ")
    cipher, full_key, plain, c_nums, k_nums, p_nums = vigenere_decrypt(text, key)

    print("\nCiphertext:      ", " ".join(cipher))
    print("Ciphertext (num):", c_nums)
    print("Key:             ", " ".join(full_key))
    print("Key (num):       ", k_nums)
    print("Plaintext:       ", " ".join(plain))
    print("Plaintext (num): ", p_nums)
    print("\nFinal Plaintext:", plain)
