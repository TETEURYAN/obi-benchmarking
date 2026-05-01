
def solve():
    line1 = input().split()
    N, B = int(line1[0]), int(line1[1])
    files = list(map(int, input().split()))
    
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

solve()
