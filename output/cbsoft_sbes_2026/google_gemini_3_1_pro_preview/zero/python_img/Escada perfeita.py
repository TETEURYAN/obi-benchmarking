
import sys

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    a = [int(x) for x in input_data[1:n+1]]
    
    total_stones = sum(a)
    base_sum = n * (n - 1) // 2
    
    rem = total_stones - base_sum
    
    if rem % n != 0:
        print("-1")
        return
        
    x = rem // n
    if x < 1:
        print("-1")
        return
        
    moves = 0
    for i in range(n):
        target = x + i
        if a[i] > target:
            moves += a[i] - target
            
    print(moves)

if __name__ == '__main__':
    main()
