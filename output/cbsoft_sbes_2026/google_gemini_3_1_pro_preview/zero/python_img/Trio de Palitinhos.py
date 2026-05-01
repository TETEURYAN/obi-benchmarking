import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    N = int(input_data[0])
    A = [int(x) for x in input_data[1:N+1]]
    
    A.sort()
    
    ans = 0
    for i in range(2, N):
        j = 0
        k = i - 1
        while j < k:
            if A[j] + A[k] > A[i]:
                ans += k - j
                k -= 1
            else:
                j += 1
                
    print(ans)

if __name__ == '__main__':
    solve()