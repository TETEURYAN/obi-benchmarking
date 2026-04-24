import sys

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    n = int(data[0])
    reposts = list(map(int, data[1:]))
    
    reposts.sort(reverse=True)
    
    ans = 0
    for i in range(n):
        if reposts[i] >= i + 1:
            ans = i + 1
        else:
            break
    print(ans)

if __name__ == "__main__":
    solve()