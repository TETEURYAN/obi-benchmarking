
import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    N = int(input_data[0])
    E = int(input_data[1])
    
    P_plus = []
    P_minus = []
    P_set = set()
    
    idx = 2
    for _ in range(E):
        V = int(input_data[idx]) - 1
        D = int(input_data[idx+1])
        idx += 2
        
        P_set.add(V)
        if D == 1:
            P_plus.append(V)
        else:
            P_minus.append(V)
            
    if P_plus:
        p0 = P_plus[0]
        candidates = [(p - p0) % N for p in P_set]
    else:
        p0 = P_minus[0]
        candidates = [(p0 - p) % N for p in P_set]
        
    candidates = [N if c == 0 else c for c in candidates]
    candidates.sort()
    
    for t in candidates:
        new_P = {(p + t) % N for p in P_plus}
        new_P.update((p - t) % N for p in P_minus)
        
        if len(new_P) == E and new_P == P_set:
            print(t)
            return

if __name__ == '__main__':
    solve()
