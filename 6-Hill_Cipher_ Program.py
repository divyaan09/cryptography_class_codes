# Hill Cipher Program (2x2 key matrix)

MOD = 26

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def mod_inverse(a, m):
    a = a % m
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

def determinant(matrix):
    return (matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]) % MOD

def is_invertible(matrix):
    det = determinant(matrix)
    return gcd(det, MOD) == 1, det

def matrix_inverse(matrix):
    det = determinant(matrix)
    det_inv = mod_inverse(det, MOD)
    if det_inv is None:
        return None
    a, b = matrix[0]
    c, d = matrix[1]
    # adjugate matrix, then multiply by det_inv, mod 26
    inv = [
        [ (d * det_inv) % MOD, (-b * det_inv) % MOD ],
        [ (-c * det_inv) % MOD, (a * det_inv) % MOD ]
    ]
    return inv

def clean(text):
    text = "".join(ch for ch in text.upper() if ch.isalpha())
    if len(text) % 2 != 0:
        text += 'X'  # pad if odd length
    return text

def to_pairs(text):
    return [(ord(text[i])-65, ord(text[i+1])-65) for i in range(0, len(text), 2)]

def multiply(matrix, pair):
    p1, p2 = pair
    r1 = (matrix[0][0]*p1 + matrix[0][1]*p2) % MOD
    r2 = (matrix[1][0]*p1 + matrix[1][1]*p2) % MOD
    return r1, r2

def to_text(pairs):
    return "".join(chr(x+65) + chr(y+65) for x, y in pairs)

def hill_encrypt(text, matrix):
    text = clean(text)
    pairs = to_pairs(text)
    cipher_pairs = [multiply(matrix, p) for p in pairs]
    return to_text(cipher_pairs)

def hill_decrypt(cipher, matrix):
    inv = matrix_inverse(matrix)
    pairs = to_pairs(cipher)
    plain_pairs = [multiply(inv, p) for p in pairs]
    return to_text(plain_pairs)

# ---- Main ----
print("Enter 2x2 key matrix values:")
a = int(input("a11: "))
b = int(input("a12: "))
c = int(input("a21: "))
d = int(input("a22: "))
matrix = [[a, b], [c, d]]

ok, det = is_invertible(matrix)
print(f"\nDeterminant = {det} mod {MOD}")
if not ok:
    print(f"Key matrix is NOT invertible mod {MOD} (gcd({det},{MOD}) != 1). Cannot proceed.")
else:
    det_inv = mod_inverse(det, MOD)
    print(f"Key matrix IS invertible. Modular inverse of determinant = {det_inv}")
    inv_matrix = matrix_inverse(matrix)
    print("Inverse key matrix:", inv_matrix)

    mode = input("\nEncrypt or Decrypt? (e/d): ")
    if mode == 'e':
        text = input("Enter plaintext: ")
        cipher = hill_encrypt(text, matrix)
        print("Ciphertext:", cipher)
    else:
        text = input("Enter ciphertext: ")
        plain = hill_decrypt(text, matrix)
        print("Plaintext:", plain)
