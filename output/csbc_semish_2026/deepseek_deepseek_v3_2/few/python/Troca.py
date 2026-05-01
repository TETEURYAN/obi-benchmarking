import sys
sys.setrecursionlimit(200000)

def main():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    N = int(next(it))
    T = int(next(it))
    
    up = [int(next(it)) for _ in range(N)]
    down = [int(next(it)) for _ in range(N)]
    
    diff = [0] * (N + 2)
    
    for _ in range(T):
        I = int(next(it)) - 1
        J = int(next(it)) - 1
        diff[I] ^= 1
        diff[J + 1] ^= 1
    
    flip = 0
    for i in range(N):
        flip ^= diff[i]
        if flip:
            up[i], down[i] = down[i], up[i]
    
    sys.stdout.write(' '.join(map(str, up)))

if __name__ == "__main__":
    main()