import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    N = int(input_data[0])
    B = int(input_data[1])
    files = [int(x) for x in input_data[2:]]
    
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
            folders += 1
        else:
            right -= 1
            folders += 1
            
    print(folders)

if __name__ == '__main__':
    solve()