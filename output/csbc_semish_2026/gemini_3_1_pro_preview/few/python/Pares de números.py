import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    N = int(input_data[0])
    I = int(input_data[1])
    F = int(input_data[2])
    
    arr = [int(x) for x in input_data[3:3+N]]
    arr.sort()
    
    def count_pairs(target):
        count = 0
        left = 0
        right = N - 1
        while left < right:
            if arr[left] + arr[right] <= target:
                count += right - left
                left += 1
            else:
                right -= 1
        return count

    ans = count_pairs(F) - count_pairs(I - 1)
    print(ans)

if __name__ == '__main__':
    solve()