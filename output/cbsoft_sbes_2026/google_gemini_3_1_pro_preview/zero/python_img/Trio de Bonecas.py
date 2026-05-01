
import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    N = int(data[0])
    K = int(data[1])
    T = sorted([int(x) for x in data[2:N+2]], reverse=True)
    
    prev2 = [float('inf')] * (K + 1)
    prev1 = [float('inf')] * (K + 1)
    prev2[0] = prev1[0] = 0
    
    for i in range(3, N + 1):
        cost = (T[i-2] - T[i-1]) ** 2
        max_j = i // 3
        if max_j > K:
            max_j = K
            
        part = [p2_cost if (p2_cost := p2 + cost) < p1 else p1 for p1, p2 in zip(prev1[1:max_j+1], prev2[:max_j])]
        new_curr = [0] + part + prev1[max_j+1:]
                
        prev2 = prev1
        prev1 = new_curr

    print(prev1[K])

if __name__ == '__main__':
    solve()
