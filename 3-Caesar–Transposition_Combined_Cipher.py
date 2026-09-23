# Caesar-Transposition Combined Cipher (Caesar + Rail Fence)

# ---- Caesar Cipher ----
def caesar_encrypt(text, shift):
    result = ""
    for ch in text:
        if ch.isalpha():
            base = ord('A') if ch.isupper() else ord('a')
            result += chr((ord(ch) - base + shift) % 26 + base)
        else:
            result += ch
    return result

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)

# ---- Rail Fence Cipher ----
def railfence_encrypt(text, rails):
    fence = [[] for _ in range(rails)]
    row, direction = 0, 1

    for ch in text:
        fence[row].append(ch)
        if row == 0:
            direction = 1
        elif row == rails - 1:
            direction = -1
        row += direction

    return "".join("".join(r) for r in fence)

def railfence_decrypt(cipher, rails):
    n = len(cipher)
    pattern = []
    row, direction = 0, 1
    for _ in range(n):
        pattern.append(row)
        if row == 0:
            direction = 1
        elif row == rails - 1:
            direction = -1
        row += direction

    rail_lengths = [pattern.count(r) for r in range(rails)]
    rail_chars = []
    idx = 0
    for length in rail_lengths:
        rail_chars.append(list(cipher[idx:idx+length]))
        idx += length

    rail_pos = [0] * rails
    result = ""
    for r in pattern:
        result += rail_chars[r][rail_pos[r]]
        rail_pos[r] += 1
    return result

# ---- Main ----
mode = input("Encrypt or Decrypt? (e/d): ")
shift = int(input("Enter Caesar shift key: "))
rails = int(input("Enter number of rails: "))

if mode == 'e':
    text = input("Enter plaintext: ")

    stage1 = caesar_encrypt(text, shift)
    print("After Caesar Cipher:", stage1)

    stage2 = railfence_encrypt(stage1, rails)
    print("After Rail Fence Cipher:", stage2)

    print("Final Ciphertext:", stage2)

else:
    text = input("Enter ciphertext: ")

    stage1 = railfence_decrypt(text, rails)
    print("After Reverse Rail Fence:", stage1)

    stage2 = caesar_decrypt(stage1, shift)
    print("After Reverse Caesar:", stage2)

    print("Final Plaintext:", stage2)
