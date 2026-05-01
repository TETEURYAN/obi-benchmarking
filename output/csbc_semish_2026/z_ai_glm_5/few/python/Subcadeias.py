import sys

def solve():
    # Leitura rápida de toda a entrada
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return

    # O primeiro elemento é N
    n = int(input_data[0])
    
    # O restante forma a string. Usamos join para juntar caso haja espaços (embora o problema sugira uma string contínua)
    # e fatiamos para garantir o comprimento N.
    s = "".join(input_data[1:])[:n]
    
    if n == 0:
        print(0)
        return

    max_len = 0
    
    # Algoritmo "Expand Around Center" (Expandir ao redor do centro)
    # Complexidade: O(N^2), adequado para N <= 500.
    for i in range(n):
        # 1. Palíndromos de comprimento ímpar (centro em i)
        l, r = i, i
        while l >= 0 and r < n and s[l] == s[r]:
            current_len = r - l + 1
            if current_len > max_len:
                max_len = current_len
            l -= 1
            r += 1
            
        # 2. Palíndromos de comprimento par (centro entre i e i+1)
        l, r = i, i + 1
        while l >= 0 and r < n and s[l] == s[r]:
            current_len = r - l + 1
            if current_len > max_len:
                max_len = current_len
            l -= 1
            r += 1
            
    print(max_len)

if __name__ == "__main__":
    solve()