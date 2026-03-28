import sys

def solve():
    data = sys.stdin.read().split()
    n = int(data[0])
    p = [int(data[i+1]) for i in range(n)]
    
    # dark[i] = 1 if segment between lamp i and lamp (i+1)%n is dark
    dark = [0] * n
    for i in range(n):
        if p[i] + p[(i+1) % n] < 1000:
            dark[i] = 1
    
    # If all segments are dark, answer is n
    if sum(dark) == n:
        print(n)
        return
    
    # Find max consecutive dark segments in circular array
    # Since not all are dark, we can linearize by doubling
    max_count = 0
    current = 0
    # Double the array to handle circular case
    for i in range(2 * n):
        if dark[i % n] == 1:
            current += 1
            if current > max_count:
                max_count = current
        else:
            current = 0
    
    # Cap at n
    if max_count > n:
        max_count = n
    
    print(max_count)

solve()