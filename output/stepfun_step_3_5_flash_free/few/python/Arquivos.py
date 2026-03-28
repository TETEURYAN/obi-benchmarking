import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    n = int(data[0])
    B = int(data[1])
    sizes = list(map(int, data[2:2+n]))
    sizes.sort()
    i = 0
    j = n - 1
    folders = 0
    while i <= j:
        if i == j:
            folders += 1
            break
        if sizes[i] + sizes[j] <= B:
            folders += 1
            i += 1
            j -= 1
        else:
            folders += 1
            j -= 1
    print(folders)

if __name__ == "__main__":
    main()