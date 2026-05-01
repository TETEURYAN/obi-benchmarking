import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    N = int(input_data[0])
    A = [int(x) for x in input_data[1:N+1]]
    
    invisible_count = 0
    max_h = 0
    
    for i in range(N - 1, -1, -1):
        if A[i] > max_h:
            max_h = A[i]
        else:
            invisible_count += 1
            
    print(invisible_count)

if __name__ == '__main__':
    solve()