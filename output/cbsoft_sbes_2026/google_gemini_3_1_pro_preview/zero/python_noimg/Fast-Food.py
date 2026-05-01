
import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    N = int(input_data[0])
    
    # Lendo as coordenadas e transformando para distância de Chebyshev
    # U = X + Y
    # V = X - Y
    x0 = int(input_data[1])
    y0 = int(input_data[1 + N])
    U_min = U_max = x0 + y0
    V_min = V_max = x0 - y0
    
    points = [(U_min, V_min)]
    
    for i in range(1, N):
        x = int(input_data[i + 1])
        y = int(input_data[i + 1 + N])
        u = x + y
        v = x - y
        points.append((u, v))
        
        if u < U_min: U_min = u
        elif u > U_max: U_max = u
        
        if v < V_min: V_min = v
        elif v > V_max: V_max = v
        
    # Busca binária pela menor distância máxima K
    low = 0
    high = max(U_max - U_min, V_max - V_min)
    ans = high
    
    while low <= high:
        mid = (low + high) // 2
        
        U_min_K = U_min + mid
        V_min_K = V_min + mid
        U_max_K = U_max - mid
        V_max_K = V_max - mid
        
        possible = False
        
        # Condição 1: Quadrado 1 cobre (U_min, V_min) e Quadrado 2 cobre (U_max, V_max)
        for u, v in points:
            if (u <= U_min_K and v <= V_min_K) or (u >= U_max_K and v >= V_max_K):
                continue
            break
        else:
            possible = True
            
        # Condição 2: Quadrado 1 cobre (U_min, V_max) e Quadrado 2 cobre (U_max, V_min)
        if not possible:
            for u, v in points:
                if (u <= U_min_K and v >= V_max_K) or (u >= U_max_K and v <= V_min_K):
                    continue
                break
            else:
                possible = True
                
        if possible:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
            
    print(ans)

if __name__ == '__main__':
    solve()
