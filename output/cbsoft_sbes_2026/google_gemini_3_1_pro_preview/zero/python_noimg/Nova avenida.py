import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    M = int(input_data[1])
    nums = list(map(int, input_data[2:]))
    
    min_sum = min(sum(nums[j::M]) for j in range(M))
    print(min_sum)

if __name__ == '__main__':
    solve()