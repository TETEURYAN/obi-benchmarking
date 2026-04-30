
import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    N = int(input_data[0])
    A = [int(x) for x in input_data[1:N+1]]
    
    max_kadane = 0
    current_max = 0
    min_kadane = 0
    current_min = 0
    total_sum = 0
    
    for x in A:
        total_sum += x
        
        current_max += x
        if current_max < 0:
            current_max = 0
        if current_max > max_kadane:
            max_kadane = current_max
            
        current_min += x
        if current_min > 0:
            current_min = 0
        if current_min < min_kadane:
            min_kadane = current_min
            
    ans = max(max_kadane, total_sum - min_kadane)
    print(ans)

if __name__ == '__main__':
    solve()
