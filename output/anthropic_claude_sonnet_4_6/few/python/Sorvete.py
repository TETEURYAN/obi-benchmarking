import sys

def solve():
    data = sys.stdin.read().split()
    idx = 0
    test_num = 0
    
    while idx < len(data):
        P = int(data[idx]); S = int(data[idx+1])
        idx += 2
        
        if P == 0 and S == 0:
            break
        
        test_num += 1
        intervals = []
        for _ in range(S):
            U = int(data[idx]); V = int(data[idx+1])
            idx += 2
            intervals.append((U, V))
        
        # Merge intervals
        intervals.sort()
        merged = []
        for u, v in intervals:
            if merged and u <= merged[-1][1]:
                merged[-1] = (merged[-1][0], max(merged[-1][1], v))
            else:
                merged.append((u, v))
        
        print(f"Teste {test_num}")
        for u, v in merged:
            print(u, v)
        print()

solve()