
import sys

def main():
    data = sys.stdin.read().split()
    ptr = 0
    test_num = 1
    while True:
        S = int(data[ptr])
        ptr += 1
        if S == 0:
            break
        coords = []
        for _ in range(S):
            x = int(data[ptr])
            y = int(data[ptr+1])
            coords.append((x, y))
            ptr += 2
        if not coords:
            print(f"Teste {test_num}")
            print("0 0")
            print()
            test_num += 1
            continue
        xs = [x for x, y in coords]
        ys = [y for x, y in coords]
        x_med = sorted(xs)[len(xs) // 2]
        y_med = sorted(ys)[len(ys) // 2]
        print(f"Teste {test_num}")
        print(f"{x_med} {y_med}")
        print()
        test_num += 1

if __name__ == "__main__":
    main()
