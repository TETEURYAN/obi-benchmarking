
import sys

def main():
    data = sys.stdin.read().split()
    idx = 0
    test_num = 1
    while idx < len(data):
        N = int(data[idx])
        idx += 1
        if N == 0:
            break
        if N == 0:
            break
        regions = []
        for _ in range(N):
            x = int(data[idx])
            y = int(data[idx+1])
            u = int(data[idx+2])
            v = int(data[idx+3])
            idx += 4
            regions.append((x, y, u, v))
        if not regions:
            print(f"Teste {test_num}")
            print("nenhum")
            print()
            test_num += 1
            continue
        x1, y1, x2, y2 = regions[0]
        for i in range(1, N):
            xi, yi, ui, vi = regions[i]
            x1 = max(x1, xi)
            y1 = min(y1, yi)
            x2 = min(x2, ui)
            y2 = max(y2, vi)
        if x1 > x2 or y1 < y2:
            print(f"Teste {test_num}")
            print("nenhum")
        else:
            print(f"Teste {test_num}")
            print(f"{x1} {y1} {x2} {y2}")
        print()
        test_num += 1

if __name__ == "__main__":
    main()
