import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    N = int(input_data[0])
    A = [int(x) for x in input_data[1:N+1]]
    
    A.sort()
    
    ans = 0
    for k in range(2, N):
        i = 0
        j = k - 1
        while i < j:
            if A[i] + A[j] > A[k]:
                ans += j - i
                j -= 1
            else:
                i += 1
                
    print(ans)

if __name__ == '__main__':
    solve()