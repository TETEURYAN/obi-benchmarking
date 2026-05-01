import sys

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    n = data[0]
    h = data[1:1+n]

    left_max = [0] * n
    mx = 0
    for i in range(n):
        if h[i] > mx:
            mx = h[i]
        left_max[i] = mx

    right_max = [0] * n
    mx = 0
    for i in range(n - 1, -1, -1):
        if h[i] > mx:
            mx = h[i]
        right_max[i] = mx

    ans = 0
    for i in range(n):
        water_level = left_max[i] if left_max[i] < right_max[i] else right_max[i]
        if water_level - h[i] >= 1:
            ans += 1

    print(ans)

if __name__ == "__main__":
    main()
