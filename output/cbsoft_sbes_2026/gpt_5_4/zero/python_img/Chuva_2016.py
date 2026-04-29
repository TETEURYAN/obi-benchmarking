import sys

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    n = data[0]
    h = data[1:1+n]

    left = [0] * n
    right = [0] * n

    mx = 0
    for i in range(n):
        if h[i] > mx:
            mx = h[i]
        left[i] = mx

    mx = 0
    for i in range(n - 1, -1, -1):
        if h[i] > mx:
            mx = h[i]
        right[i] = mx

    ans = 0
    for i in range(n):
        if min(left[i], right[i]) - h[i] >= 1:
            ans += 1

    print(ans)

if __name__ == "__main__":
    main()
