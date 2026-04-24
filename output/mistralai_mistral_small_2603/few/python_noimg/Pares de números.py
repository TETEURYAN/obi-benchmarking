
import sys

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    I = int(data[1])
    F = int(data[2])
    arr = list(map(int, data[3:3+n]))
    arr.sort()
    count = 0
    left = 0
    right = n - 1
    while left < right:
        s = arr[left] + arr[right]
        if s >= I:
            count += right - left
            right -= 1
        else:
            left += 1
    left = 0
    right = n - 1
    count2 = 0
    while left < right:
        s = arr[left] + arr[right]
        if s > F:
            count2 += right - left
            right -= 1
        else:
            left += 1
    print(count - count2)

if __name__ == "__main__":
    main()
