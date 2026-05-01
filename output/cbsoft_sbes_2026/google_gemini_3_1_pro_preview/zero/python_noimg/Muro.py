import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    
    if n == 0:
        print(1)
        return
    if n == 1:
        print(1)
        return
    if n == 2:
        print(5)
        return
        
    MOD = 10**9 + 7
    
    f0 = 1
    f1 = 1
    f2 = 5
    
    for _ in range(3, n + 1):
        f3 = (f2 + 4 * f1 + 2 * f0) % MOD
        f0 = f1
        f1 = f2
        f2 = f3
        
    print(f2)

if __name__ == '__main__':
    solve()