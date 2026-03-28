import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    H = data[0].strip()
    V = data[1].strip()
    
    max_j = {}
    for idx, letra in enumerate(V, start=1):
        max_j[letra] = idx
    
    encontrado = False
    for i in range(len(H), 0, -1):
        letra = H[i-1]
        if letra in max_j:
            print(i, max_j[letra])
            encontrado = True
            break
    
    if not encontrado:
        print("-1 -1")

if __name__ == "__main__":
    main()