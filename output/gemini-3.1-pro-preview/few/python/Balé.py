import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    a = [int(x) for x in input_data[1:n+1]]
    
    sorted_a = sorted(list(set(a)))
    rank = {val: i + 1 for i, val in enumerate(sorted_a)}
    
    bit = [0] * (len(rank) + 1)
    
    def add(idx, val):
        while idx < len(bit):
            bit[idx] += val
            idx += idx & (-idx)
            
    def query(idx):
        s = 0
        while idx > 0:
            s += bit[idx]
            idx -= idx & (-idx)
        return s

    inversions = 0
    for i in range(n - 1, -1, -1):
        r = rank[a[i]]
        inversions += query(r - 1)
        add(r, 1)
        
    print(inversions)

if __name__ == '__main__':
    solve()