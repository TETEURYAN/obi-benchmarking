import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    iterator = iter(input_data)
    try:
        next(iterator)
        K_str = next(iterator)
    except StopIteration:
        return
        
    K = int(K_str)
    
    freq = {0: 1}
    curr_sum = 0
    ans = 0
    
    for s in iterator:
        curr_sum += int(s)
        target = curr_sum - K
        if target in freq:
            ans += freq[target]
        
        if curr_sum in freq:
            freq[curr_sum] += 1
        else:
            freq[curr_sum] = 1
            
    print(ans)

if __name__ == '__main__':
    solve()