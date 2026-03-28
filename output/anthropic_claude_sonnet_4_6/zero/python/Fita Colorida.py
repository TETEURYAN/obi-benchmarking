
import sys

def main():
    input_data = sys.stdin.read().split()
    n = int(input_data[0])
    tape = list(map(int, input_data[1:n+1]))
    
    result = [9] * n
    
    # Forward pass
    dist = float('inf')
    for i in range(n):
        if tape[i] == 0:
            dist = 0
        else:
            if dist < float('inf'):
                dist += 1
        result[i] = min(result[i], dist)
    
    # Backward pass
    dist = float('inf')
    for i in range(n-1, -1, -1):
        if tape[i] == 0:
            dist = 0
        else:
            if dist < float('inf'):
                dist += 1
        result[i] = min(result[i], dist)
    
    # Cap at 9
    result = [min(x, 9) for x in result]
    
    print(' '.join(map(str, result)))

main()
