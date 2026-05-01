
import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    N = int(input_data[0])
    V = [int(x) for x in input_data[1:N+1]]
    
    pos = {}
    for idx, x in enumerate(V):
        if x not in pos:
            pos[x] = []
        pos[x].append(idx)
        
    unique_V = list(pos.keys())
    if len(unique_V) <= 1:
        print(1 if N > 0 else 0)
        return
        
    max_len = 1
    
    for i in range(len(unique_V)):
        a = unique_V[i]
        p_a = pos[a]
        for j in range(i + 1, len(unique_V)):
            b = unique_V[j]
            p_b = pos[b]
            
            count = 0
            last = -1
            idx_a = 0
            idx_b = 0
            
            while idx_a < len(p_a) and idx_b < len(p_b):
                if p_a[idx_a] < p_b[idx_b]:
                    if last != a:
                        count += 1
                        last = a
                    idx_a += 1
                else:
                    if last != b:
                        count += 1
                        last = b
                    idx_b += 1
                    
            if last != a and idx_a < len(p_a):
                count += 1
            if last != b and idx_b < len(p_b):
                count += 1
                
            if count > max_len:
                max_len = count
                
    print(max_len)

if __name__ == '__main__':
    solve()
