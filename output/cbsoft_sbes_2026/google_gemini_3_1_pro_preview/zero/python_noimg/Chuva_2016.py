import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    N = int(input_data[0])
    H = [int(x) for x in input_data[1:]]
    
    if not H:
        print(0)
        return
        
    n = len(H)
    left_max = [0] * n
    right_max = [0] * n
    
    left_max[0] = H[0]
    for i in range(1, n):
        left_max[i] = max(left_max[i-1], H[i])
        
    right_max[n-1] = H[n-1]
    for i in range(n-2, -1, -1):
        right_max[i] = max(right_max[i+1], H[i])
        
    ans = 0
    for i in range(n):
        if min(left_max[i], right_max[i]) > H[i]:
            ans += 1
            
    print(ans)

if __name__ == '__main__':
    solve()