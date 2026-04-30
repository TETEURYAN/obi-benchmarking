import sys
import math

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    A = int(input_data[0])
    B = int(input_data[1])
    
    if A % 2 != 0:
        print("-1 -1")
        return
        
    S = (A + 4) // 2
    P = A + B
    
    delta = S * S - 4 * P
    if delta < 0:
        print("-1 -1")
        return
        
    root_delta = math.isqrt(delta)
    if root_delta * root_delta != delta:
        print("-1 -1")
        return
        
    if (S - root_delta) % 2 != 0:
        print("-1 -1")
        return
        
    W = (S - root_delta) // 2
    L = (S + root_delta) // 2
    
    if W >= 3 and L >= 3 and (W - 2) * (L - 2) == B:
        print(f"{W} {L}")
    else:
        print("-1 -1")

if __name__ == '__main__':
    solve()