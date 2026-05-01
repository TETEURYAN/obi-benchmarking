import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    N = int(input_data[0])
    A = [int(x) for x in input_data[1:N+1]]
    
    bit = [0] * (N + 1)
    inversions = 0
    
    for i, x in enumerate(A):
        s = 0
        idx = x
        while idx > 0:
            s += bit[idx]
            idx -= idx & (-idx)
            
        inversions += i - s
        
        idx = x
        while idx <= N:
            bit[idx] += 1
            idx += idx & (-idx)
            
    print(inversions)

if __name__ == '__main__':
    solve()