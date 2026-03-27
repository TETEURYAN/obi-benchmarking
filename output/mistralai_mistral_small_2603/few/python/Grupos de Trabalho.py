
import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return

    idx = 0
    E = int(data[idx])
    M = int(data[idx+1])
    D = int(data[idx+2])
    idx += 3

    same = set()
    for _ in range(M):
        x = int(data[idx])
        y = int(data[idx+1])
        if x > y:
            x, y = y, x
        same.add((x, y))
        idx += 2

    diff = set()
    for _ in range(D):
        u = int(data[idx])
        v = int(data[idx+1])
        if u > v:
            u, v = v, u
        diff.add((u, v))
        idx += 2

    groups = []
    for _ in range(E // 3):
        i = int(data[idx])
        j = int(data[idx+1])
        k = int(data[idx+2])
        groups.append((i, j, k))
        idx += 3

    violations = 0

    for group in groups:
        a, b, c = group
        students = {a, b, c}

        for pair in [(a, b), (a, c), (b, c)]:
            x, y = pair
            if x > y:
                x, y = y, x
            if (x, y) in diff:
                violations += 1

        for pair in [(a, b), (a, c), (b, c)]:
            x, y = pair
            if x > y:
                x, y = y, x
            if (x, y) in same:
                if pair not in same:
                    violations += 1

    print(violations)

if __name__ == "__main__":
    main()
