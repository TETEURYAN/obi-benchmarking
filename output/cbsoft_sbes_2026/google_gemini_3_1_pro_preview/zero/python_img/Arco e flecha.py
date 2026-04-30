
import sys
from array import array

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    N = int(input_data[0])
    
    MAX_BITS = 42
    MAX_NODES = N * (MAX_BITS + 1) + 2
    
    child = array('i', [0] * (MAX_NODES * 2))
    count = array('i', [0] * MAX_NODES)
    next_node = 1
    
    out = []
    idx = 1
    P = 0
    
    for _ in range(N):
        X = int(input_data[idx])
        Y = int(input_data[idx+1])
        idx += 2
        
        XR = X + P
        YR = Y + P
        D = XR * XR + YR * YR
        
        ans = 0
        node = 0
        for i in range(MAX_BITS, -1, -1):
            bit = (D >> i) & 1
            if bit == 1:
                left_child = child[node * 2]
                if left_child != 0:
                    ans += count[left_child]
            
            child_idx = node * 2 + bit
            nxt = child[child_idx]
            if nxt == 0:
                nxt = next_node
                child[child_idx] = nxt
                next_node += 1
            node = nxt
            count[node] += 1
            
        ans += count[node] - 1
        P = ans
        out.append(str(P))
        
    sys.stdout.write('\n'.join(out) + '\n')

if __name__ == '__main__':
    solve()
