import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    vidas = [int(x) for x in input_data[1:n+1]]
    
    max_so_far = vidas[0]
    current_max = vidas[0]
    
    for i in range(1, n):
        current_max = max(vidas[i], current_max + vidas[i])
        if current_max > max_so_far:
            max_so_far = current_max
            
    print(max_so_far)

if __name__ == '__main__':
    solve()