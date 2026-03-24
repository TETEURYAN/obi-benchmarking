import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    N = int(input_data[0])
    nums = [int(x) for x in input_data[1:]]
    
    if len(nums) != N * N:
        print(0)
        return
        
    if min(nums) != 1 or max(nums) != N * N or len(set(nums)) != N * N:
        print(0)
        return
        
    target_sum = sum(nums[0:N])
    
    for i in range(1, N):
        if sum(nums[i*N : (i+1)*N]) != target_sum:
            print(0)
            return
            
    for j in range(N):
        if sum(nums[j::N]) != target_sum:
            print(0)
            return
            
    if sum(nums[0 :: N+1]) != target_sum:
        print(0)
        return
        
    if sum(nums[N-1 : N*N - N + 1 : N-1]) != target_sum:
        print(0)
        return
        
    print(target_sum)

if __name__ == '__main__':
    solve()