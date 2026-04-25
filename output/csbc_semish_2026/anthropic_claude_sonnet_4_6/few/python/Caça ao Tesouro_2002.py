import sys

def solve():
    data = sys.stdin.read().split()
    idx = 0
    test_num = 0
    
    while idx < len(data):
        X = int(data[idx]); Y = int(data[idx+1]); N = int(data[idx+2])
        idx += 3
        
        if X == 0 and Y == 0 and N == 0:
            break
        
        test_num += 1
        items = []
        for i in range(N):
            items.append(int(data[idx]))
            idx += 1
        
        total_chest = sum(items)
        total = X + Y + total_chest
        
        # We need to split chest items into two groups A and B
        # such that X + sum(A) == Y + sum(B)
        # and sum(A) + sum(B) = total_chest
        # X + sum(A) == Y + total_chest - sum(A)
        # 2*sum(A) = Y + total_chest - X
        # sum(A) = (Y + total_chest - X) / 2
        
        diff = Y + total_chest - X
        if diff < 0 or diff % 2 != 0:
            print(f"Teste {test_num}")
            print("N")
            print()
            continue
        
        target = diff // 2
        
        # Check if target > total_chest
        if target > total_chest:
            print(f"Teste {test_num}")
            print("N")
            print()
            continue
        
        # Subset sum: can we pick subset of items summing to target?
        dp = [False] * (target + 1)
        dp[0] = True
        
        for v in items:
            if v > target:
                continue
            for s in range(target, v - 1, -1):
                if dp[s - v]:
                    dp[s] = True
        
        print(f"Teste {test_num}")
        print("S" if dp[target] else "N")
        print()

solve()