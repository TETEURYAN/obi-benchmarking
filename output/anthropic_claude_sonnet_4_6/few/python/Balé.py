import sys
from sortedcontainers import SortedList

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    skills = list(map(int, data[1:n+1]))
    
    # A valid pair (i, j) where i < j (i is older) requires:
    # skill[i] > skill[j] (the older one is more skilled)
    # So we need to count pairs (i, j) with i < j and skills[i] > skills[j]
    # This is the count of inversions
    
    # Use a Fenwick Tree (BIT) to count inversions
    max_val = 100001
    bit = [0] * (max_val + 1)
    
    def update(i):
        while i <= max_val:
            bit[i] += 1
            i += i & (-i)
    
    def query(i):
        s = 0
        while i > 0:
            s += bit[i]
            i -= i & (-i)
        return s
    
    count = 0
    for idx in range(n):
        s = skills[idx]
        # Count elements already inserted that are greater than s
        # = idx - query(s)
        count += idx - query(s)
        update(s)
    
    print(count)

main()