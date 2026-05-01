import sys

def main():
    data = list(map(int, sys.stdin.read().split()))
    if not data:
        return
    n = data[0]
    a = data[1:1+n]

    last = a[-1]
    best_i = -1
    best_val = -1

    if last != 0:
        for i in range(n - 1):
            if a[i] == 0 and a[i] > last:
                if a[i] > best_val:
                    best_val = a[i]
                    best_i = i

    if last != 5:
        for i in range(n - 1):
            if a[i] == 5 and a[i] > last:
                if a[i] > best_val:
                    best_val = a[i]
                    best_i = i

    if best_i != -1:
        a[best_i], a[-1] = a[-1], a[best_i]
        print(*a)
        return

    target = 0 if any(x == 0 for x in a[:-1]) else (5 if any(x == 5 for x in a[:-1]) else -1)
    if target == -1:
        print(-1)
        return

    for i in range(n - 1):
        if a[i] < target:
            continue
        if a[i] == target:
            continue
        if a[i] > target:
            continue

    pos = -1
    for i in range(n - 1):
        if a[i] == target:
            pos = i
            break

    if pos == -1:
        print(-1)
        return

    best_j = -1
    best_digit = -1
    for j in range(pos + 1, n):
        if a[j] > best_digit:
            best_digit = a[j]
            best_j = j

    if best_j == -1:
        print(-1)
        return

    a[pos], a[best_j] = a[best_j], a[pos]
    print(*a)

if __name__ == "__main__":
    main()
