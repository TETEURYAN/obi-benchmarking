
import sys

input = sys.stdin.read
data = input().split()

N = int(data[0])
weights = list(map(int, data[1:]))

if N == 0:
    print("S")
    sys.exit()

max_weight = weights[-1]

if max_weight > 8:
    can = False
    for w in weights:
        if w <= 8:
            can = True
            break
    if not can:
        print("N")
        sys.exit()

weights.sort(reverse=True)

left = 0
right = N - 1
possible = True

while left <= right:
    if left == right:
        if weights[left] > 8:
            possible = False
        break
    
    heavy = weights[left]
    light = weights[right]
    
    if heavy > 8:
        if light > 8:
            possible = False
            break
        if heavy - light > 8:
            possible = False
            break
        left += 1
        right -= 1
    else:
        if heavy - 0 > 8:
            possible = False
            break
        left += 1

if possible:
    print("S")
else:
    print("N")
```

**Explanation:** The solution uses a two-pointer greedy approach after sorting the weights in descending order. It simulates pairing the heaviest remaining box with the lightest one (or empty cabin) while ensuring the weight difference never exceeds 8. Single heavy boxes (>8) must be paired with a sufficiently light box. The algorithm efficiently checks feasibility in O(N log N) time due to sorting, which is acceptable for N ≤ 10