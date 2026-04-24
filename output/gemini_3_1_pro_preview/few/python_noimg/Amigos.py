import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    k = int(input_data[1])
    
    a_indices = []
    b_indices = []
    
    for i in range(n):
        if input_data[2 + i] == '1':
            a_indices.append(i)
            
    for i in range(n):
        if input_data[2 + n + i] == '1':
            b_indices.append(i)
            
    ans = 0
    for i in range(k):
        ans += abs(a_indices[i] - b_indices[i])
        
    print(ans)

if __name__ == '__main__':
    solve()