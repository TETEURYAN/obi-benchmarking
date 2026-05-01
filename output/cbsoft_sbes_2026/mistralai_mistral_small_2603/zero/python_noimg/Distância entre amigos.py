
import sys

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    a = list(map(int, data[1:n+1]))

    max_dist = 0
    max_left = [0] * n
    max_right = [0] * n

    max_left[0] = a[0]
    for i in range(1, n):
        max_left[i] = max(max_left[i-1], a[i])

    max_right[-1] = a[-1]
    for i in range(n-2, -1, -1):
        max_right[i] = max(max_right[i+1], a[i])

    for i in range(n):
        if i == 0:
            current = max_right[i+1] + a[i] + 1
        elif i == n-1:
            current = max_left[i-1] + a[i] + 1
        else:
            current = max(max_left[i-1], max_right[i+1]) + a[i] + 1
        if current > max_dist:
            max_dist = current

    print(max_dist)

if __name__ == "__main__":
    main()
