
import sys

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    N = int(data[0])
    B = int(data[1])
    files = list(map(int, data[2:2+N]))
    
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
