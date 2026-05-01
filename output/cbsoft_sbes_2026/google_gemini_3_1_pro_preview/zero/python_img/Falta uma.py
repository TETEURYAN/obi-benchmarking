import sys

def solve():
    def get_ints():
        for line in sys.stdin:
            for token in line.split():
                yield int(token)
                
    token_iter = get_ints()
    try:
        N = next(token_iter)
    except StopIteration:
        return
        
    counts = [[0] * (N + 1) for _ in range(N)]
    
    j = 0
    for val in token_iter:
        counts[j][val] += 1
        j += 1
        if j == N:
            j = 0
            
    ans = [str(min(range(1, N + 1), key=lambda k: counts[j][k])) for j in range(N)]
    print(" ".join(ans))

if __name__ == '__main__':
    solve()