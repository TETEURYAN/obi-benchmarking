import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    N = int(next(it))
    B = int(next(it))
    files = [int(next(it)) for _ in range(N)]
    files.sort()
    left = 0
    right = N - 1
    folders = 0
    while left <= right:
        if left == right:
            folders += 1
            break
        if files[left] + files[right] <= B:
            left += 1
            right -= 1
        else:
            right -= 1
        folders += 1
    print(folders)

if __name__ == "__main__":
    main()