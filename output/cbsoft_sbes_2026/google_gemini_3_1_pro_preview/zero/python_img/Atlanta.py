import sys
import math

def main():
    input_data = sys.stdin.read().split()
    if len(input_data) < 2:
        return
    A = int(input_data[0])
    B = int(input_data[1])
    
    if (A - 4) % 2 != 0:
        print("-1 -1")
        return
        
    S = (A - 4) // 2
    if S <= 0:
        print("-1 -1")
        return
        
    Delta = S * S - 4 * B
    if Delta < 0:
        print("-1 -1")
        return
        
    d = math.isqrt(Delta)
    if d * d != Delta:
        print("-1 -1")
        return
        
    if (S - d) % 2 != 0:
        print("-1 -1")
        return
        
    w = (S - d) // 2
    l = (S + d) // 2
    
    if w >= 1 and l >= 1:
        print(f"{w + 2} {l + 2}")
    else:
        print("-1 -1")

if __name__ == '__main__':
    main()