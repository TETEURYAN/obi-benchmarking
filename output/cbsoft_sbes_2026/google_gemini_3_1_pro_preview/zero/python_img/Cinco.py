
import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    N = int(input_data[0])
    D = [int(x) for x in input_data[1:N+1]]
    
    last_digit = D[-1]
    best_i = -1
    
    for i in range(N - 1):
        if D[i] in (0, 5) and D[i] < last_digit:
            best_i = i
            break
            
    if best_i != -1:
        D[best_i], D[-1] = D[-1], D[best_i]
        print(*(D))
        return
        
    for i in range(N - 2, -1, -1):
        if D[i] in (0, 5):
            best_i = i
            break
            
    if best_i != -1:
        D[best_i], D[-1] = D[-1], D[best_i]
        print(*(D))
        return
        
    print("-1")

if __name__ == '__main__':
    solve()
