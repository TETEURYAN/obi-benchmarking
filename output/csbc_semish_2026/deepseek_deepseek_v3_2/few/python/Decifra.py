import sys

def main():
    data = sys.stdin.read().splitlines()
    if not data:
        return
    
    perm = data[0].strip()
    encrypted = data[1].strip()
    
    # Construir o mapeamento inverso: de letra criptografada para original
    decrypt_map = {}
    for i, ch in enumerate(perm):
        original_char = chr(ord('a') + i)
        decrypt_map[ch] = original_char
    
    # Decifrar cada caractere
    result = []
    for ch in encrypted:
        result.append(decrypt_map[ch])
    
    print(''.join(result))

if __name__ == "__main__":
    main()