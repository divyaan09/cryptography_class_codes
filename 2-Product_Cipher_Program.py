# Product Cipher - Substitution + Transposition

# ---- Substitution Cipher (Caesar Shift) ----
def substitute(text, shift):
    result = ""
    for ch in text:
        if ch.isalpha():
            base = ord('A') if ch.isupper() else ord('a')
            result += chr((ord(ch) - base + shift) % 26 + base)
        else:
            result += ch
    return result

def unsubstitute(text, shift):
    return substitute(text, -shift)

# ---- Columnar Transposition Cipher ----
def transpose(text, key):
    text = text.replace(" ", "")
    cols = len(key)
    rows = -(-len(text) // cols)  # ceil division
    padded = text.ljust(rows * cols, 'X')

    grid = [padded[i:i+cols] for i in range(0, len(padded), cols)]
    order = sorted(range(cols), key=lambda i: key[i])

    result = ""
    for col in order:
        for row in grid:
            result += row[col]
    return result

def untranspose(text, key):
    cols = len(key)
    rows = len(text) // cols
    order = sorted(range(cols), key=lambda i: key[i])

    grid = [""] * cols
    idx = 0
    for col in order:
        grid[col] = text[idx:idx+rows]
        idx += rows

    result = ""
    for r in range(rows):
        for c in range(cols):
            result += grid[c][r]
    return result

# ---- Main ----
mode = input("Encrypt or Decrypt? (e/d): ")
shift = int(input("Enter substitution shift key: "))
key = input("Enter transposition key (e.g. 3142): ")

if mode == 'e':
    text = input("Enter plaintext: ")
    stage1 = substitute(text, shift)
    print("After Substitution:", stage1)

    stage2 = transpose(stage1, key)
    print("After Transposition:", stage2)

    print("Final Ciphertext:", stage2)

else:
    text = input("Enter ciphertext: ")
    stage1 = untranspose(text, key)
    print("After Reverse Transposition:", stage1)

    stage2 = unsubstitute(stage1, shift)
    print("After Reverse Substitution:", stage2)

    print("Final Plaintext:", stage2)
