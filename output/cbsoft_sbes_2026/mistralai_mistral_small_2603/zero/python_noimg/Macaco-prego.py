
import sys

def main():
    data = sys.stdin.read().split()
    ptr = 0
    test_num = 1
    while ptr < len(data):
        N = int(data[ptr])
        ptr += 1
        if N == 0:
            break
        if N == 0:
            print(f"Teste {test_num}")
            print("nenhum")
            print()
            test_num += 1
            continue
        regions = []
        for _ in range(N):
            x = int(data[ptr])
            y = int(data[ptr+1])
            u = int(data[ptr+2])
            v = int(data[ptr+3])
            ptr += 4
            regions.append((x, y, u, v))
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
