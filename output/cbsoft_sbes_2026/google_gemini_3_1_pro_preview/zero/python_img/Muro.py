
import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    
    MOD = 10**9 + 7
    
    if n == 0:
        print(1)
        return
    if n == 1:
        print(1)
        return
    if n == 2:
        print(5)
        return
        
    a, b, c = 1, 1, 5
    for _ in range(3, n + 1):
        next_val = (c + 4 * b + 2 * a) % MOD
        a, b, c = b, c, next_val
        
    print(c)

if __name__ == '__main__':
    solve()
