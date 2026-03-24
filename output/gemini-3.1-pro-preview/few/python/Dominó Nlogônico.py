import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    x = [int(v) for v in input_data[1:n+1]]
    h = [int(v) for v in input_data[n+1:2*n+1]]
    
    r = [0] * n
    stack = []
    
    for i in range(n - 1, -1, -1):
        r[i] = i
        limit = x[i] + h[i]
        while stack and x[stack[-1]] <= limit:
            k = stack.pop()
            if r[k] > r[i]:
                r[i] = r[k]
        stack.append(i)
        
    ans = [str(r[i] - i + 1) for i in range(n)]
    print(" ".join(ans))

if __name__ == '__main__':
    solve()