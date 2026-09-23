def mod_inverse(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

def encrypt(text, key):
    result = ""
    text = text.upper()

    for ch in text:
        if ch.isalpha():
            p = ord(ch) - ord('A')
            c = (p * key) % 26
            result += chr(c + ord('A'))
        else:
            result += ch
    return result

def decrypt(cipher, key):
    result = ""
    cipher = cipher.upper()

    inv = mod_inverse(key, 26)
    if inv is None:
        return "Key has no modular inverse. Choose another key."

    for ch in cipher:
        if ch.isalpha():
            c = ord(ch) - ord('A')
            p = (c * inv) % 26
            result += chr(p + ord('A'))
        else:
            result += ch
    return result

if __name__ == "__main__":
    mode = input("Mode (encrypt/decrypt): ").strip().lower()
    key = int(input("Enter key: "))

    if mode == "encrypt":
        text = input("Enter plaintext: ")
        print("Ciphertext:", encrypt(text, key))

    elif mode == "decrypt":
        text = input("Enter ciphertext: ")
        print("Plaintext:", decrypt(text, key))

    else:
        print("Invalid mode.")
