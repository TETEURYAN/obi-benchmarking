import sys

sys.setrecursionlimit(200000)

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    if n == 0:
        print(0)
        return
        
    h = [int(x) for x in input_data[1:n+1]]
    
    left_max = [0] * n
    right_max = [0] * n
    
    left_max[0] = h[0]
    for i in range(1, n):
        left_max[i] = max(left_max[i-1], h[i])
        
    right_max[n-1] = h[n-1]
    for i in range(n-2, -1, -1):
        right_max[i] = max(right_max[i+1], h[i])
        
    count = 0
    for i in range(n):
        if min(left_max[i], right_max[i]) > h[i]:
            count += 1
            
    print(count)

if __name__ == '__main__':
    solve()