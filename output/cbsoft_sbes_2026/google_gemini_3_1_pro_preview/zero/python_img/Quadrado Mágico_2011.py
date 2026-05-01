
import sys

def solve():
    def get_ints():
        for line in sys.stdin:
            for token in line.split():
                yield int(token)
                
    tokens = get_ints()
    
    try:
        N = next(tokens)
    except StopIteration:
        return
        
    seen = bytearray(N * N + 1)
    
    col_sums = [0] * N
    diag1_sum = 0
    diag2_sum = 0
    
    expected_sum = -1
    limit = N * N
    
    for i in range(N):
        row_sum = 0
        for j in range(N):
            val = next(tokens)
            
            if val < 1 or val > limit or seen[val]:
                print(0)
                return
            seen[val] = 1
            
            row_sum += val
            col_sums[j] += val
            if i == j:
                diag1_sum += val
            if i + j == N - 1:
                diag2_sum += val
                
        if i == 0:
            expected_sum = row_sum
        elif row_sum != expected_sum:
            print(0)
            return

    for j in range(N):
        if col_sums[j] != expected_sum:
            print(0)
            return
            
    if diag1_sum != expected_sum or diag2_sum != expected_sum:
        print(0)
        return
        
    print(expected_sum)

if __name__ == '__main__':
    solve()
