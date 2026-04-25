import sys

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    weights = list(map(int, data))
    weights.sort()
    
    # Tentar todas as combinações para o topo (1 cubo)
    for i in range(6):
        top = weights[i]
        # Remover o cubo do topo
        remaining = weights[:i] + weights[i+1:]
        
        # Tentar todas as combinações para o meio (2 cubos)
        for j in range(5):
            for k in range(j+1, 5):
                middle = remaining[j] + remaining[k]
                # Os 3 cubos restantes formam a base
                base_indices = [idx for idx in range(5) if idx != j and idx != k]
                base = remaining[base_indices[0]] + remaining[base_indices[1]] + remaining[base_indices[2]]
                
                if top == middle == base:
                    print('S')
                    return
    
    print('N')

if __name__ == "__main__":
    solve()