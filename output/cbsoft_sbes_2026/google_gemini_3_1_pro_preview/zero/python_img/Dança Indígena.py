
import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    N = int(input_data[0])
    E = int(input_data[1])
    
    P = [0] * E
    D = [0] * E
    
    in_S = [False] * N
    
    idx = 2
    for i in range(E):
        P[i] = int(input_data[idx]) - 1
        D[i] = int(input_data[idx+1])
        in_S[P[i]] = True
        idx += 2
        
    candidates = []
    P0 = P[0]
    D0 = D[0]
    for j in range(E):
        t = (D0 * (P[j] - P0)) % N
        if t == 0:
            t = N
        candidates.append(t)
        
    candidates = sorted(list(set(candidates)))
    
    visited_for_t = [-1] * N
    
    for t in candidates:
        valid = True
        for i in range(E):
            pos = (P[i] + D[i] * t) % N
            if not in_S[pos]:
                valid = False
                break
            if visited_for_t[pos] == t:
                valid = False
                break
            visited_for_t[pos] = t
        if valid:
            print(t)
            break

if __name__ == '__main__':
    solve()
