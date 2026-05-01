import sys

sys.setrecursionlimit(200000)

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    N = int(input_data[0])
    
    X = [int(x) for x in input_data[1:N+1]]
    Y = [int(x) for x in input_data[N+1:2*N+1]]
    
    U = [x + y for x, y in zip(X, Y)]
    V = [x - y for x, y in zip(X, Y)]
    
    U_min = min(U)
    U_max = max(U)
    V_min = min(V)
    V_max = max(V)
    
    points = list(zip(U, V))
    
    low = 0
    high = max(U_max - U_min, V_max - V_min)
    ans = high
    
    while low <= high:
        mid = (low + high) // 2
        
        U_min_mid = U_min + mid
        V_min_mid = V_min + mid
        U_max_mid = U_max - mid
        V_max_mid = V_max - mid
        
        valid1 = True
        for u, v in points:
            if u <= U_min_mid and v <= V_min_mid:
                continue
            if u >= U_max_mid and v >= V_max_mid:
                continue
            valid1 = False
            break
            
        if valid1:
            ans = mid
            high = mid - 1
            continue
            
        valid2 = True
        for u, v in points:
            if u <= U_min_mid and v >= V_max_mid:
                continue
            if u >= U_max_mid and v <= V_min_mid:
                continue
            valid2 = False
            break
            
        if valid2:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
            
    print(ans)

if __name__ == '__main__':
    solve()