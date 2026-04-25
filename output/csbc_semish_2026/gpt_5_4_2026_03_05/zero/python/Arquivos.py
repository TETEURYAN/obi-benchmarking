import sys

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    n, b = data[0], data[1]
    a = data[2:2+n]
    a.sort()
    
    i, j = 0, n - 1
    folders = 0
    
    while i <= j:
        if i == j:
            folders += 1
            break
        if a[i] + a[j] <= b:
            i += 1
            j -= 1
        else:
            j -= 1
        folders += 1
    
    print(folders)

if __name__ == "__main__":
    main()
