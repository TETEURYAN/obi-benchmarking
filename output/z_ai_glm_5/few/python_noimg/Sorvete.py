
import sys

def solve():
    data = sys.stdin.read().split()
    idx = 0
    test_num = 1
    
    while idx < len(data):
        P = int(data[idx])
        S = int(data[idx + 1])
        idx += 2
        
        if P == 0 and S == 0:
            break
        
        intervals = []
        for _ in range(S):
            U = int(data[idx])
            V = int(data[idx + 1])
            intervals.append((U, V))
            idx += 2
        
        intervals.sort()
        
        merged = []
        for start, end in intervals:
            if not merged or start > merged[-1][1]:
                merged.append([start, end])
            else:
                merged[-1][1] = max(merged[-1][1], end)
        
        print(f"Teste {test_num}")
        for start, end in merged:
            print(f"{start} {end}")
        print()
        
        test_num += 1

solve()
