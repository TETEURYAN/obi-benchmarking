import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    N = int(input_data[0])
    L = [int(x) for x in input_data[1:N+1]]
    
    total_C = sum(L)
    
    if total_C % 2 != 0:
        print('N')
        return
        
    target = total_C // 2
    
    positions = [0] * N
    current_pos = 0
    for i in range(N):
        positions[i] = current_pos
        current_pos += L[i]
        
    count = 0
    i = 0
    j = 0
    
    while i < N and j < N:
        diff = positions[j] - positions[i]
        if diff == target:
            count += 1
            if count >= 2:
                print('S')
                return
            i += 1
            j += 1
        elif diff < target:
            j += 1
        else:
            i += 1
            
    print('N')

if __name__ == '__main__':
    solve()