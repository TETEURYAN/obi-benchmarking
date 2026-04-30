import sys
from bisect import bisect_left

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    C = int(input_data[0])
    T = int(input_data[1])
    
    R2 = [0] * C
    for i in range(C):
        r = int(input_data[2 + i])
        R2[i] = r * r
        
    total_score = 0
    idx = 2 + C
    for _ in range(T):
        x = int(input_data[idx])
        y = int(input_data[idx+1])
        idx += 2
        
        d2 = x * x + y * y
        pos = bisect_left(R2, d2)
        total_score += C - pos
        
    print(total_score)

if __name__ == '__main__':
    main()