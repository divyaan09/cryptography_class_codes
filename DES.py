INITIAL_PERM = [58, 50, 42, 34, 26, 18, 10, 2, 60, 52, 44, 36, 28, 20, 12, 4,
                62, 54, 46, 38, 30, 22, 14, 6, 64, 56, 48, 40, 32, 24, 16, 8,
                57, 49, 41, 33, 25, 17, 9, 1, 59, 51, 43, 35, 27, 19, 11, 3,
                61, 53, 45, 37, 29, 21, 13, 5, 63, 55, 47, 39, 31, 23, 15, 7]

FINAL_PERM = [40, 8, 48, 16, 56, 24, 64, 32, 39, 7, 47, 15, 55, 23, 63, 31,
              38, 6, 46, 14, 54, 22, 62, 30, 37, 5, 45, 13, 53, 21, 61, 29,
              36, 4, 44, 12, 52, 20, 60, 28, 35, 3, 43, 11, 51, 19, 59, 27,
              34, 2, 42, 10, 50, 18, 58, 26, 33, 1, 41, 9, 49, 17, 57, 25]

EXPANSION = [32, 1, 2, 3, 4, 5, 4, 5, 6, 7, 8, 9, 8, 9, 10, 11, 12, 13,
             12, 13, 14, 15, 16, 17, 16, 17, 18, 19, 20, 21, 20, 21, 22,
             23, 24, 25, 24, 25, 26, 27, 28, 29, 28, 29, 30, 31, 32, 1]

STRAIGHT_PERM = [16, 7, 20, 21, 29, 12, 28, 17, 1, 15, 23, 26, 5, 18, 31, 10,
                  2, 8, 24, 14, 32, 27, 3, 9, 19, 13, 30, 6, 22, 11, 4, 25]

KEY_PERM_1 = [57, 49, 41, 33, 25, 17, 9, 1, 58, 50, 42, 34, 26, 18, 10, 2,
              59, 51, 43, 35, 27, 19, 11, 3, 60, 52, 44, 36, 63, 55, 47, 39,
              31, 23, 15, 7, 62, 54, 46, 38, 30, 22, 14, 6, 61, 53, 45, 37,
              29, 21, 13, 5, 28, 20, 12, 4]

KEY_PERM_2 = [14, 17, 11, 24, 1, 5, 3, 28, 15, 6, 21, 10, 23, 19, 12, 4,
              26, 8, 16, 7, 27, 20, 13, 2, 41, 52, 31, 37, 47, 55, 30, 40,
              51, 45, 33, 48, 44, 49, 39, 56, 34, 53, 46, 42, 50, 36, 29, 32]

ROTATIONS = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]

SBOXES = [
    [[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
     [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
     [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
     [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]],
    [[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
     [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
     [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
     [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]],
    [[10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
     [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
     [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
     [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]],
    [[7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
     [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
     [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
     [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]],
    [[2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
     [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
     [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
     [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]],
    [[12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
     [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
     [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
     [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]],
    [[4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
     [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
     [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
     [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]],
    [[13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
     [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
     [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
     [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]],
]


def apply_table(source_bits, table):
    """Rearrange bits according to a permutation/expansion table (1-indexed)."""
    return [source_bits[pos - 1] for pos in table]


def bitwise_xor(bits_a, bits_b):
    return [a ^ b for a, b in zip(bits_a, bits_b)]


def rotate_left(bits, amount):
    return bits[amount:] + bits[:amount]


def text_to_bits(raw_bytes):
    out = []
    for byte in raw_bytes:
        out.extend(int(b) for b in f"{byte:08b}")
    return out


def bits_to_bytes(bits):
    chunks = [bits[i:i + 8] for i in range(0, len(bits), 8)]
    return bytes(int("".join(map(str, c)), 2) for c in chunks)


def build_round_keys(key_bytes):
    """Turn an 8-byte key into the 16 subkeys used, one per round."""
    bits56 = apply_table(text_to_bits(key_bytes), KEY_PERM_1)
    left, right = bits56[:28], bits56[28:]

    round_keys = []
    for shift_amount in ROTATIONS:
        left = rotate_left(left, shift_amount)
        right = rotate_left(right, shift_amount)
        round_keys.append(apply_table(left + right, KEY_PERM_2))
    return round_keys


def f_function(half_block, round_key):
    expanded = apply_table(half_block, EXPANSION)
    mixed = bitwise_xor(expanded, round_key)

    substituted = []
    for box_index in range(8):
        chunk = mixed[box_index * 6:box_index * 6 + 6]
        row = chunk[0] * 2 + chunk[5]
        col = chunk[1] * 8 + chunk[2] * 4 + chunk[3] * 2 + chunk[4]
        value = SBOXES[box_index][row][col]
        substituted.extend(int(b) for b in f"{value:04b}")

    return apply_table(substituted, STRAIGHT_PERM)


def process_block(block_bits, round_keys, reverse):
    bits = apply_table(block_bits, INITIAL_PERM)
    left, right = bits[:32], bits[32:]

    key_order = reversed(round_keys) if reverse else round_keys
    for round_key in key_order:
        left, right = right, bitwise_xor(left, f_function(right, round_key))

    return apply_table(right + left, FINAL_PERM)


def add_padding(data):
    pad_len = 8 - (len(data) % 8)
    return data + bytes([pad_len] * pad_len)


def strip_padding(data):
    return data[:-data[-1]]


def normalize_key(user_key):
    """Force any key text into exactly 8 bytes."""
    key_bytes = user_key.encode("utf-8")
    return key_bytes.ljust(8, b"0")[:8]


def encrypt(message, user_key):
    key_bytes = normalize_key(user_key)
    round_keys = build_round_keys(key_bytes)

    padded = add_padding(message.encode("utf-8"))
    cipher_bytes = bytearray()
    for offset in range(0, len(padded), 8):
        block = padded[offset:offset + 8]
        cipher_bits = process_block(text_to_bits(block), round_keys, reverse=False)
        cipher_bytes.extend(bits_to_bytes(cipher_bits))

    return cipher_bytes.hex()


def decrypt(hex_ciphertext, user_key):
    key_bytes = normalize_key(user_key)
    round_keys = build_round_keys(key_bytes)

    cipher_bytes = bytes.fromhex(hex_ciphertext)
    plain_bytes = bytearray()
    for offset in range(0, len(cipher_bytes), 8):
        block = cipher_bytes[offset:offset + 8]
        plain_bits = process_block(text_to_bits(block), round_keys, reverse=True)
        plain_bytes.extend(bits_to_bytes(plain_bits))

    return strip_padding(bytes(plain_bytes)).decode("utf-8")


def main():
    print("=== My DES Tool ===")
    choice = input("Type 'e' to encrypt or 'd' to decrypt: ").strip().lower()
    key = input("Your key (any text, will be adjusted to 8 bytes): ")

    if choice == "e":
        message = input("Text to encrypt: ")
        print("\nCiphertext (hex):", encrypt(message, key))
    elif choice == "d":
        hex_text = input("Hex ciphertext to decrypt: ").strip()
        try:
            print("\nRecovered text:", decrypt(hex_text, key))
        except Exception:
            print("Couldn't decrypt — wrong key or corrupted ciphertext.")
    else:
        print("Please type 'e' or 'd'.")
        sys.exit(1)


if __name__ == "__main__":
    main()
