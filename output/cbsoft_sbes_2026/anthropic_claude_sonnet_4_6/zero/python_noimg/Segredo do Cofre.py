import sys
input = sys.stdin.readline

def main():
    N, M = map(int, input().split())
    bar = list(map(int, input().split()))
    positions = list(map(int, input().split()))
    
    # Build prefix sums for each digit 0-9
    # prefix[d][i] = count of digit d in bar[0..i-1]
    prefix = [[0] * (N + 1) for _ in range(10)]
    for i in range(N):
        for d in range(10):
            prefix[d][i+1] = prefix[d][i]
        prefix[bar[i]][i+1] += 1
    
    def count_in_range(l, r, d):
        # 1-indexed, inclusive [l, r]
        return prefix[d][r] - prefix[d][l-1]
    
    total = [0] * 10
    
    # The control slides between consecutive positions
    # When sliding from pos A to pos B, the range covered is [min(A,B), max(A,B)]
    # But we need to count each position only once per visit
    # Actually, re-reading: we count how many times each integer appears "inside the control"
    # The control passes through all positions between consecutive stops
    # Each segment [A, B] contributes positions min(A,B) to max(A,B)
    # But overlapping segments should count multiple times
    
    for i in range(M - 1):
        a = positions[i]
        b = positions[i+1]
        l = min(a, b)
        r = max(a, b)
        for d in range(10):
            total[d] += count_in_range(l, r, d)
    
    # But the starting position is counted in the first segment
    # Each intermediate stop position is counted twice (end of one segment, start of next)
    # We need to subtract the intermediate positions (positions[1] to positions[M-2])
    for i in range(1, M - 1):
        p = positions[i]
        d = bar[p - 1]
        total[d] -= 1
    
    print(*total)

main()