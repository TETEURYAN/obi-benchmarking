
import sys

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    L = int(data[1])
    R = int(data[2])
    a = list(map(int, data[3:3+n]))

    a_sorted = sorted(a)
    max_diff = 0

    for i in range(n):
        current = a_sorted[i]
        if i == 0:
            diff = a_sorted[i+1] - current
        elif i == n-1:
            diff = current - a_sorted[i-1]
        else:
            diff = min(current - a_sorted[i-1], a_sorted[i+1] - current)
        if diff > max_diff:
            max_diff = diff

    max_possible = max_diff
    if max_possible == 0:
        print(0)
        return

    candidates = []
    for num in a_sorted:
        if num - max_possible >= L:
            candidates.append(num - max_possible)
        if num + max_possible <= R:
            candidates.append(num + max_possible)

    if not candidates:
        print(0)
        return

    best = -10**18
    for x in candidates:
        if x < L or x > R:
            continue
        min_diff = 10**18
        for num in a_sorted:
            diff = abs(x - num)
            if diff < min_diff:
                min_diff = diff
        if min_diff > best:
            best = min_diff

    print(best)

if __name__ == "__main__":
    main()
