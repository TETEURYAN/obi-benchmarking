import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    n = int(data[0])
    factors = {
        1: {},
        2: {2: 1},
        3: {3: 1},
        4: {2: 2},
        5: {5: 1},
        6: {2: 1, 3: 1},
        7: {7: 1},
        8: {2: 3},
        9: {3: 2}
    }
    num = {2: 0, 3: 0, 5: 0, 7: 0}
    den = {2: 0, 3: 0, 5: 0, 7: 0}
    idx = 1
    for _ in range(n):
        d = int(data[idx])
        op = data[idx + 1]
        idx += 2
        fac = factors[d]
        if op == '*':
            for p, exp in fac.items():
                num[p] += exp
        else:
            for p, exp in fac.items():
                den[p] += exp
    result = 1
    for p in (2, 3, 5, 7):
        diff = num[p] - den[p]
        if diff > 0:
            result *= p ** diff
    print(result)

if __name__ == "__main__":
    main()