
import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    N = int(input_data[0])
    K = int(input_data[1])
    
    freq = {0: 1}
    current_sum = 0
    
    for i in range(2, len(input_data)):
        current_sum += int(input_data[i])
        if current_sum in freq:
            freq[current_sum] += 1
        else:
            freq[current_sum] = 1
            
    ans = 0
    if K == 0:
        for count in freq.values():
            if count > 1:
                ans += count * (count - 1) // 2
    else:
        for val, count in freq.items():
            target = val - K
            if target in freq:
                ans += count * freq[target]
                
    print(ans)

if __name__ == '__main__':
    solve()
