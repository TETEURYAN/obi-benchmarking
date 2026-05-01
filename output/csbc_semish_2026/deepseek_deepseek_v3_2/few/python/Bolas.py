import sys
from collections import Counter

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    balls = list(map(int, data))
    freq = Counter(balls)
    
    # Condição necessária: a maior frequência <= 4
    # (pois com 8 posições, se uma cor aparece 5 vezes, pelo menos 2 serão adjacentes)
    # Mas precisamos verificar também casos como 4-4, 4-2-2, etc.
    max_freq = max(freq.values())
    if max_freq > 4:
        print("N")
        return
    
    # Para 8 bolas, podemos usar backtracking (8! = 40320 estados)
    # Mas otimizamos verificando permutações únicas das cores
    colors = list(freq.keys())
    counts = list(freq.values())
    
    def backtrack(pos, last):
        if pos == 8:
            return True
        
        for i in range(len(colors)):
            if counts[i] == 0:
                continue
            if colors[i] == last:
                continue
            counts[i] -= 1
            if backtrack(pos + 1, colors[i]):
                return True
            counts[i] += 1
        return False
    
    result = backtrack(0, -1)
    print("S" if result else "N")

if __name__ == "__main__":
    main()