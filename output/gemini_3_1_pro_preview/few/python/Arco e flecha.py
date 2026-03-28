import sys
import array

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    
    MAX_NODES = 42 * n + 2
    left = array.array('i', [0] * MAX_NODES)
    right = array.array('i', [0] * MAX_NODES)
    count = array.array('i', [0] * MAX_NODES)
    node_cnt = 1
    
    out = []
    idx = 1
    P = 0
    
    for _ in range(n):
        x = int(input_data[idx]) + P
        y = int(input_data[idx+1]) + P
        idx += 2
        
        D = x * x + y * y
        
        curr = 1
        ans = 0
        for i in range(41, -1, -1):
            if curr == 0:
                break
            if (D >> i) & 1:
                l_child = left[curr]
                if l_child != 0:
                    ans += count[l_child]
                curr = right[curr]
            else:
                curr = left[curr]
        if curr != 0:
            ans += count[curr]
            
        P = ans
        out.append(str(P))
        
        curr = 1
        count[curr] += 1
        for i in range(41, -1, -1):
            if (D >> i) & 1:
                nxt = right[curr]
                if nxt == 0:
                    node_cnt += 1
                    right[curr] = node_cnt
                    nxt = node_cnt
                curr = nxt
            else:
                nxt = left[curr]
                if nxt == 0:
                    node_cnt += 1
                    left[curr] = node_cnt
                    nxt = node_cnt
                curr = nxt
            count[curr] += 1

    print('\n'.join(out))

if __name__ == '__main__':
    solve()