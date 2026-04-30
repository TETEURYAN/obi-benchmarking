import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    N = int(input_data[0])
    F = int(input_data[1])
    C = [int(x) for x in input_data[2:N+2]]
    
    low = 1
    high = 10**18
    ans = high
    
    while low <= high:
        mid = (low + high) // 2
        
        coins = 0
        for c in C:
            coins += mid // c
            if coins >= F:
                break
                
        if coins >= F:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
            
    print(ans)

if __name__ == '__main__':
    solve()