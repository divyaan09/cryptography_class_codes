# Playfair Cipher Program

def build_matrix(key):
    key = key.upper().replace("J", "I")
    seen = []
    for ch in key:
        if ch.isalpha() and ch not in seen:
            seen.append(ch)
    for ch in "ABCDEFGHIKLMNOPQRSTUVWXYZ":  # no J
        if ch not in seen:
            seen.append(ch)

    matrix = [seen[i*5:(i+1)*5] for i in range(5)]
    return matrix

def print_matrix(matrix):
    for row in matrix:
        print(" ".join(row))

def find_pos(matrix, ch):
    for r in range(5):
        for c in range(5):
            if matrix[r][c] == ch:
                return r, c
    return None

def prepare_text(text):
    text = "".join(ch for ch in text.upper() if ch.isalpha()).replace("J", "I")
    pairs = []
    i = 0
    while i < len(text):
        a = text[i]
        b = text[i+1] if i+1 < len(text) else 'X'
        if a == b:
            pairs.append((a, 'X'))
            i += 1
        else:
            pairs.append((a, b))
            i += 2
    return pairs

def encrypt_pair(matrix, a, b):
    r1, c1 = find_pos(matrix, a)
    r2, c2 = find_pos(matrix, b)
    if r1 == r2:
        return matrix[r1][(c1+1)%5], matrix[r2][(c2+1)%5]
    elif c1 == c2:
        return matrix[(r1+1)%5][c1], matrix[(r2+1)%5][c2]
    else:
        return matrix[r1][c2], matrix[r2][c1]

def decrypt_pair(matrix, a, b):
    r1, c1 = find_pos(matrix, a)
    r2, c2 = find_pos(matrix, b)
    if r1 == r2:
        return matrix[r1][(c1-1)%5], matrix[r2][(c2-1)%5]
    elif c1 == c2:
        return matrix[(r1-1)%5][c1], matrix[(r2-1)%5][c2]
    else:
        return matrix[r1][c2], matrix[r2][c1]

def playfair_encrypt(text, matrix):
    pairs = prepare_text(text)
    result = ""
    print("\nDigraphs:", pairs)
    for a, b in pairs:
        ea, eb = encrypt_pair(matrix, a, b)
        result += ea + eb
    return result

def playfair_decrypt(cipher, matrix):
    cipher = "".join(ch for ch in cipher.upper() if ch.isalpha())
    result = ""
    for i in range(0, len(cipher), 2):
        a, b = cipher[i], cipher[i+1]
        da, db = decrypt_pair(matrix, a, b)
        result += da + db
    return result

# ---- Main ----
key = input("Enter keyword for key matrix: ")
matrix = build_matrix(key)

print("\n5x5 Key Matrix:")
print_matrix(matrix)

mode = input("\nEncrypt or Decrypt? (e/d): ")

if mode == 'e':
    text = input("Enter plaintext: ")
    cipher = playfair_encrypt(text, matrix)
    print("\nCiphertext:", cipher)
else:
    text = input("Enter ciphertext: ")
    plain = playfair_decrypt(text, matrix)
    print("\nPlaintext:", plain)
    print("(Note: any 'X' inserted for repeated letters or padding may need manual removal)")
