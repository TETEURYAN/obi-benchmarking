import sys

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    N = int(input_data[0])
    F = int(input_data[1])
    
    C = [int(x) for x in input_data[2:N+2]]
    
    left = 1
    right = 10**8
    ans = right
    
    while left <= right:
        mid = (left + right) // 2
        
        total_coins = 0
        for c in C:
            total_coins += mid // c
            if total_coins >= F:
                break
                
        if total_coins >= F:
            ans = mid
            right = mid - 1
        else:
            left = mid + 1
            
    print(ans)

if __name__ == '__main__':
    main()