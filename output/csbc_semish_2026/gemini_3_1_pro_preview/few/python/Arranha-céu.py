import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    N = int(input_data[0])
    Q = int(input_data[1])
    
    A = [0] * (N + 1)
    bit = [0] * (N + 1)
    
    def add(idx, val):
        while idx <= N:
            bit[idx] += val
            idx += idx & (-idx)
            
    def query(idx):
        s = 0
        while idx > 0:
            s += bit[idx]
            idx -= idx & (-idx)
        return s

    idx = 2
    for i in range(1, N + 1):
        val = int(input_data[idx])
        A[i] = val
        add(i, val)
        idx += 1
        
    out = []
    for _ in range(Q):
        type = int(input_data[idx])
        if type == 0:
            K = int(input_data[idx+1])
            P = int(input_data[idx+2])
            diff = P - A[K]
            A[K] = P
            add(K, diff)
            idx += 3
        else:
            K = int(input_data[idx+1])
            out.append(str(query(K)))
            idx += 2
            
    if out:
        sys.stdout.write('\n'.join(out) + '\n')

if __name__ == '__main__':
    solve()