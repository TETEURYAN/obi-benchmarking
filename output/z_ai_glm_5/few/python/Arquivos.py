import sys

def solve():
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return

    iterator = iter(input_data)
    try:
        n = int(next(iterator))
        b = int(next(iterator))
        sizes = []
        for _ in range(n):
            sizes.append(int(next(iterator)))
    except StopIteration:
        return

    sizes.sort()

    left = 0
    right = n - 1
    folders = 0

    while left <= right:
        if sizes[left] + sizes[right] <= b:
            left += 1
        right -= 1
        folders += 1

    print(folders)

if __name__ == '__main__':
    solve()