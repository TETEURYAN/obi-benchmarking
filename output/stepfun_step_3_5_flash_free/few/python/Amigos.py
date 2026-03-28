import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    N = int(next(it))
    K = int(next(it))
    a = [int(next(it)) for _ in range(N)]
    b = [int(next(it)) for _ in range(N)]
    a_pos = [i+1 for i, val in enumerate(a) if val == 1]
    b_pos = [i+1 for i, val in enumerate(b) if val == 1]
    total = 0
    for i in range(K):
        total += abs(a_pos[i] - b_pos[i])
    print(total)

if __name__ == "__main__":
    main()