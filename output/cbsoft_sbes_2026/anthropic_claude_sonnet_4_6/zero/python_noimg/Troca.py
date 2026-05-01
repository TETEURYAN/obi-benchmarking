import sys
from sys import stdin

def main():
    input = stdin.readline
    data = sys.stdin.read().split()
    idx = 0
    
    N, T = int(data[idx]), int(data[idx+1])
    idx += 2
    
    top = [int(data[idx+i]) for i in range(N)]
    idx += N
    bottom = [int(data[idx+i]) for i in range(N)]
    idx += N
    
    ops = []
    for _ in range(T):
        i, j = int(data[idx])-1, int(data[idx+1])-1
        idx += 2
        ops.append((i, j))
    
    # We need to determine for each position, how many times it was flipped
    # Use difference array to count flips
    # flip_count[k] = number of times position k was flipped
    # If odd -> swap top/bottom
    
    diff = [0] * (N + 1)
    for i, j in ops:
        diff[i] += 1
        if j + 1 <= N:
            diff[j+1] -= 1
    
    # Compute prefix sum
    count = 0
    result = []
    for k in range(N):
        count += diff[k]
        if count % 2 == 1:
            result.append(bottom[k])
        else:
            result.append(top[k])
    
    print(' '.join(map(str, result)))

main()