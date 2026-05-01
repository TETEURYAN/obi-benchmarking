import sys
from sys import stdin

def main():
    input = stdin.readline
    data = sys.stdin.read().split()
    idx = 0
    
    N, T = int(data[idx]), int(data[idx+1])
    idx += 2
    
    up = [int(data[idx+i]) for i in range(N)]
    idx += N
    
    down = [int(data[idx+i]) for i in range(N)]
    idx += N
    
    # We need to track which cards are flipped
    # Use a difference array to count number of flips for each position
    # If a card is flipped odd number of times, it shows the other side
    
    # diff array for range updates
    diff = [0] * (N + 1)
    
    for _ in range(T):
        i, j = int(data[idx]) - 1, int(data[idx+1]) - 1
        idx += 2
        diff[i] += 1
        if j + 1 <= N:
            diff[j+1] -= 1
    
    # Compute prefix sum to get flip count for each position
    result = []
    current = 0
    for k in range(N):
        current += diff[k]
        if current % 2 == 0:
            result.append(up[k])
        else:
            result.append(down[k])
    
    print(' '.join(map(str, result)))

main()