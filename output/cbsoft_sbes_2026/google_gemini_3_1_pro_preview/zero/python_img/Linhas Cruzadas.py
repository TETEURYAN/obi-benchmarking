
import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    N = int(input_data[0])
    A = [int(x) for x in input_data[1:N+1]]
    
    bit = [0] * (N + 1)
    
    inversions = 0
    for i in range(N - 1, -1, -1):
        x = A[i]
        
        idx = x - 1
        s = 0
        while idx > 0:
            s += bit[idx]
            idx -= idx & (-idx)
        inversions += s
        
        idx = x
        while idx <= N:
            bit[idx] += 1
            idx += idx & (-idx)
            
    print(inversions)

if __name__ == '__main__':
    solve()
