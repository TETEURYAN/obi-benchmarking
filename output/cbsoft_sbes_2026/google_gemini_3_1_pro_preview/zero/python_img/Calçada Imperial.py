
import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    N = int(input_data[0])
    V = [int(x) for x in input_data[1:N+1]]
    
    pos = {}
    for i, x in enumerate(V):
        if x not in pos:
            pos[x] = []
        pos[x].append(i)
        
    unique_V = list(pos.keys())
    if len(unique_V) <= 1:
        print(1 if N > 0 else 0)
        return
        
    max_len = 1
    for i in range(len(unique_V)):
        p_a = pos[unique_V[i]]
        len_a = len(p_a)
        for j in range(i + 1, len(unique_V)):
            p_b = pos[unique_V[j]]
            len_b = len(p_b)
            
            idx_a = 0
            idx_b = 0
            
            last = -1
            curr = 0
            
            while idx_a < len_a and idx_b < len_b:
                if p_a[idx_a] < p_b[idx_b]:
                    if last != 0:
                        curr += 1
                        last = 0
                    idx_a += 1
                else:
                    if last != 1:
                        curr += 1
                        last = 1
                    idx_b += 1
                    
            if idx_a < len_a and last != 0:
                curr += 1
            if idx_b < len_b and last != 1:
                curr += 1
                
            if curr > max_len:
                max_len = curr
                
    print(max_len)

if __name__ == '__main__':
    solve()
