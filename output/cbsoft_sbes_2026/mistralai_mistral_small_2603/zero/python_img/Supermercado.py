
import sys

def solve():
    data = sys.stdin.read().split()
    idx = 0
    test_num = 1
    while idx < len(data):
        S = int(data[idx])
        idx += 1
        if S == 0:
            break
        coords = []
        for _ in range(S):
            x = int(data[idx])
            y = int(data[idx + 1])
            coords.append((x, y))
            idx += 2
        min_x = min(coords, key=lambda c: c[0])[0]
        max_x = max(coords, key=lambda c: c[0])[0]
        min_y = min(coords, key=lambda c: c[1])[1]
        max_y = max(coords, key=lambda c: c[1])[1]
        median_x = (min_x + max_x) // 2
        median_y = (min_y + max_y) // 2
        print(f"Teste {test_num}")
        print(f"{median_x} {median_y}")
        print()
        test_num += 1

solve()
