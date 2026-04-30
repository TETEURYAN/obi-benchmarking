
import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    N = int(input_data[0])
    
    X = [int(input_data[i]) for i in range(1, N + 1)]
    Y = [int(input_data[i]) for i in range(N + 1, 2 * N + 1)]
    
    UV = [(x + y, x - y) for x, y in zip(X, Y)]
    
    u_min = min(uv[0] for uv in UV)
    u_max = max(uv[0] for uv in UV)
    v_min = min(uv[1] for uv in UV)
    v_max = max(uv[1] for uv in UV)
    
    low = 0
    high = max(u_max - u_min, v_max - v_min)
    ans = high
    
    while low <= high:
        mid = (low + high) // 2
        
        u_min_D = u_min + mid
        v_min_D = v_min + mid
        u_max_D = u_max - mid
        v_max_D = v_max - mid
        
        valid1 = True
        for u, v in UV:
            if (u <= u_min_D and v <= v_min_D) or (u >= u_max_D and v >= v_max_D):
                continue
            valid1 = False
            break
            
        if valid1:
            ans = mid
            high = mid - 1
            continue
            
        valid2 = True
        for u, v in UV:
            if (u <= u_min_D and v >= v_max_D) or (u >= u_max_D and v <= v_min_D):
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
