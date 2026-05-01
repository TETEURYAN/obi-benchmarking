import sys

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    N = int(next(it))
    M = int(next(it))
    heights = [int(next(it)) for _ in range(N)]
    
    diff = [h - M for h in heights]
    moves = 0
    for i in range(N - 1):
        if diff[i] != 0:
            moves += abs(diff[i])
            diff[i + 1] -= diff[i]
            diff[i] = 0
    print(moves)

if __name__ == "__main__":
    main()