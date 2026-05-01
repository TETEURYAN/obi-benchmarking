
import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    weights = list(map(int, input_data))
    
    total_sum = sum(weights)
    if total_sum % 3 != 0:
        print('N')
        return
        
    T = total_sum // 3
    
    if T not in weights:
        print('N')
        return
        
    weights.remove(T)
    
    found = False
    for i in range(len(weights)):
        for j in range(i + 1, len(weights)):
            if weights[i] + weights[j] == T:
                found = True
                break
        if found:
            break
            
    if found:
        print('S')
    else:
        print('N')

if __name__ == '__main__':
    solve()
