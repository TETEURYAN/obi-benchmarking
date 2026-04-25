import sys
import math

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    
    if n == 1:
        print("N")
        return

    if n % 2 == 0:
        if n == 2:
            print("N")
        else:
            print("S")
        return

    limit = math.isqrt(n)
    is_composite = False
    for i in range(3, limit + 1, 2):
        if n % i == 0:
            is_composite = True
            break
            
    if is_composite:
        print("S")
    else:
        print("N")

if __name__ == "__main__":
    solve()