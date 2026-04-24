
import sys

def main():
    data = sys.stdin.read().split()
    ptr = 0
    test_num = 1
    while True:
        if ptr >= len(data):
            break
        A = int(data[ptr])
        V = int(data[ptr + 1])
        ptr += 2
        if A == 0 and V == 0:
            break

        traffic = [0] * (A + 1)
        for _ in range(V):
            X = int(data[ptr])
            Y = int(data[ptr + 1])
            ptr += 2
            traffic[X] += 1
            traffic[Y] += 1

        max_traffic = max(traffic[1:A + 1])
        airports = [str(i) for i in range(1, A + 1) if traffic[i] == max_traffic]
        print(f"Teste {test_num}")
        print(' '.join(airports))
        print()
        test_num += 1

if __name__ == "__main__":
    main()
