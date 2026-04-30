import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    N = int(input_data[0])
    arr = [int(x) for x in input_data[1:N+1]]
    
    max_sum = 0
    current_max = 0
    
    min_sum = 0
    current_min = 0
    
    total_sum = 0
    
    for x in arr:
        total_sum += x
        
        current_max += x
        if current_max < 0:
            current_max = 0
        if current_max > max_sum:
            max_sum = current_max
            
        current_min += x
        if current_min > 0:
            current_min = 0
        if current_min < min_sum:
            min_sum = current_min
            
    ans = max(max_sum, total_sum - min_sum)
    print(ans)

if __name__ == '__main__':
    solve()