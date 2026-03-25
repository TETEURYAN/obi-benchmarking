import sys

def main():
    data = sys.stdin.read().strip().split()
    idx = 0
    test_num = 1

    while idx < len(data):
        A = int(data[idx])
        V = int(data[idx + 1])
        idx += 2

        if A == 0 and V == 0:
            break

        traffic = [0] * (A + 1)

        for _ in range(V):
            X = int(data[idx])
            Y = int(data[idx + 1])
            idx += 2
            traffic[X] += 1
            traffic[Y] += 1

        max_traffic = max(traffic[1:])
        result = []
        for airport in range(1, A + 1):
            if traffic[airport] == max_traffic:
                result.append(airport)

        print(f"Teste {test_num}")
        print(*result)
        print()
        test_num += 1

if __name__ == "__main__":
    main()