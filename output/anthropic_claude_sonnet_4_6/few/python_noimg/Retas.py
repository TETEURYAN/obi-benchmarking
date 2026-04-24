Looking at this problem, I need to count intersections between N lines where the x-coordinate of intersection falls within [X1, X2].

Two lines y = A1*x + B1 and y = A2*x + B2 intersect at x = (B2-B1)/(A1-A2) when A1 ≠ A2. If A1 = A2, they're parallel (no intersection) or identical (excluded by constraints).

The intersection x must satisfy X1 ≤ x ≤ X2, i.e., X1 ≤ (B2-B1)/(A1-A2) ≤ X2.

With N up to 10^5, O(N^2) is 10^10 which is too slow. I need a smarter approach.

Key insight: Two lines with different slopes intersect at some x. The order of lines by y-value at a given x changes exactly when two lines swap their relative order. 

At x = X1, sort lines by y-value (A*X1 + B). At x = X2, sort lines by y-value (A*X2 + B). The number of intersections in [X1, X2] equals the number of inversions between the two orderings.

But we need to handle ties carefully and also count intersections exactly at X1 or X2.

Lines with the same slope never intersect. Lines with different slopes intersect at exactly one x.

The number of pairs that swap order between X1 and X2 = number of inversions between the two sorted orders = number of intersections strictly inside (X1, X2). We also need to add intersections exactly at X1 and X2.

Actually, let me think more carefully. Sort by (y at X1, then y at X2) and count inversions in the second key - this gives intersections strictly between X1 and X2. Then add pairs that intersect exactly at X1 or X2.

For intersections at exactly X1: pairs where A1*X1+B1 = A2*X1+B2 but A1 ≠ A2.
For intersections at exactly X2: pairs where A1*X2+B1 = A2*X2+B2 but A1 ≠ A2.

Let me implement merge sort for counting inversions.

import sys
from collections import defaultdict

def merge_sort_count(arr):
    if len(arr) <= 1:
        return arr, 0
    mid = len(arr) // 2
    left, lc = merge_sort_count(arr[:mid])
    right, rc = merge_sort_count(arr[mid:])
    merged = []
    count = lc + rc
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            count += len(left) - i
            j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged, count

def solve():
    sys.setrecursionlimit(300000)
    data = sys.stdin.read().split()
    idx = 0
    N = int(data[idx]); idx+=1
    X1 = int(data[idx]); idx+=1
    X2 = int(data[idx]); idx+=1
    lines = []
    for _ in range(N):
        A = int(data[idx]); idx+=1
        B = int(data[idx]); idx+=1
        lines.append((A, B))
    
    # y at X1 and X2 using fractions to avoid float issues - use tuples (A*X+B) as integers
    # Sort by y at X1, break ties by y at X2
    def y1(line): return line[0]*X1 + line[1]
    def y2(line): return line[0]*X2 + line[1]
    
    # Sort by (y at X1, y at X2)
    lines_sorted = sorted(lines, key=lambda l: (y1(l), y2(l)))
    
    # Count intersections at exactly X1
    at_x1 = defaultdict(int)
    for l in lines:
        at_x1[y1(l)] += 1
    cnt_x1 = sum(v*(v-1)//2 for v in at_x1.values())
    
    # Count intersections at exactly X2
    at_x2 = defaultdict(int)
    for l in lines:
        at_x2[y2(l)] += 1
    cnt_x2 = sum(v*(v-1)//2 for v in at_x2.values())
    
    # Count inversions in y2 order after sorting by (y1, y2)
    # Pairs that are tied at y1 won't invert (they intersect at X1, already counted)
    y2_vals = [y2(l) for l in lines_sorted]
    _, inv = merge_sort_count(y2_vals)
    
    print(inv + cnt_x1 + cnt_x2)

solve()