
import sys
from collections import defaultdict
from math import gcd

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    n = int(data[0])
    P = int(data[1])
    Q = int(data[2])
    points = []
    idx = 3
    for _ in range(n):
        x = int(data[idx])
        y = int(data[idx+1])
        points.append((x, y))
        idx += 2

    if Q < 0:
        P = -P
        Q = -Q

    reduced_P = P // gcd(P, Q)
    reduced_Q = Q // gcd(P, Q)

    slope_counts = defaultdict(int)
    for x, y in points:
        num = y * reduced_Q
        den = x * reduced_Q
        g = gcd(num, den)
        if g != 0:
            num //= g
            den //= g
        slope = (num, den)
        slope_counts[slope] += 1

    total_pairs = 0
    slopes = list(slope_counts.keys())
    m = len(slopes)
    for i in range(m):
        num_i, den_i = slopes[i]
        for j in range(i + 1, m):
            num_j, den_j = slopes[j]
            if num_i * den_j >= num_j * den_i:
                total_pairs += slope_counts[slopes[i]] * slope_counts[slopes[j]]

    for count in slope_counts.values():
        total_pairs += count * (count - 1) // 2

    print(total_pairs)

if __name__ == "__main__":
    main()
