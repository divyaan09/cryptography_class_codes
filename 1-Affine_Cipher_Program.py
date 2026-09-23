# Affine Cipher - Basic Version

m = 26  # size of alphabet

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def mod_inverse(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

def encrypt(text, a, b):
    result = ""
    for ch in text:
        if ch.isalpha():
            base = ord('A') if ch.isupper() else ord('a')
            result += chr((a * (ord(ch) - base) + b) % m + base)
        else:
            result += ch
    return result

def decrypt(text, a, b):
    a_inv = mod_inverse(a, m)
    result = ""
    for ch in text:
        if ch.isalpha():
            base = ord('A') if ch.isupper() else ord('a')
            result += chr((a_inv * (ord(ch) - base - b)) % m + base)
        else:
            result += ch
    return result

# ---- Main ----
a = int(input("Enter key a: "))
b = int(input("Enter key b: "))

if gcd(a, m) != 1:
    print("Invalid key! 'a' must be coprime with 26.")
else:
    a_inv = mod_inverse(a, m)
    print("Modular inverse of a is:", a_inv)

    text = input("Enter text: ")
    choice = input("Encrypt or Decrypt? (e/d): ")

    if choice == 'e':
        print("Result:", encrypt(text, a, b))
    else:
        print("Result:", decrypt(text, a, b))
