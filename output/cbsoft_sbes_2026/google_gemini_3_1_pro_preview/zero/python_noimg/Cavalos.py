import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    M = int(input_data[0])
    N = int(input_data[1])
    
    if M == 1 or N == 1:
        print(M * N)
    elif M == 2 or N == 2:
        K = max(M, N)
        ans = 4 * (K // 4) + 2 * min(2, K % 4)
        print(ans)
    else:
        print((M * N + 1) // 2)

if __name__ == '__main__':
    solve()