import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    N = int(data[0])
    M = int(data[1])
    S = int(data[2])
    
    for i in range(M, N - 1, -1):
        s = 0
        x = i
        while x:
            s += x % 10
            x //= 10
        if s == S:
            print(i)
            return
    print(-1)

if __name__ == "__main__":
    main()