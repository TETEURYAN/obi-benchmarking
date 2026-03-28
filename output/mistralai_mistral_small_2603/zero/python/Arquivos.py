
import sys

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    B = int(data[1])
    sizes = list(map(int, data[2:2+n]))
    sizes.sort()
    left = 0
    right = n - 1
    folders = 0
    while left <= right:
        if sizes[left] + sizes[right] <= B:
            left += 1
        right -= 1
        folders += 1
    print(folders)

if __name__ == "__main__":
    main()
