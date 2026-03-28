import sys

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    n = int(data[0])
    energies = list(map(int, data[1:1+n]))
    
    energies.sort()
    
    # Construir a ordem ótima: padrão "zig-zag" (do meio para fora)
    result = [0] * n
    left, right = 0, n - 1
    for i in range(n):
        if i % 2 == 0:
            result[i] = energies[left]
            left += 1
        else:
            result[i] = energies[right]
            right -= 1
    
    # Calcular dissonância
    dissonance = 0
    for i in range(n):
        dissonance += abs(result[i] - result[(i + 1) % n])
    
    # Verificar ordem inversa também (outro padrão possível)
    energies_rev = energies[::-1]
    result2 = [0] * n
    left, right = 0, n - 1
    for i in range(n):
        if i % 2 == 0:
            result2[i] = energies_rev[left]
            left += 1
        else:
            result2[i] = energies_rev[right]
            right -= 1
    
    dissonance2 = 0
    for i in range(n):
        dissonance2 += abs(result2[i] - result2[(i + 1) % n])
    
    print(min(dissonance, dissonance2))

if __name__ == "__main__":
    solve()