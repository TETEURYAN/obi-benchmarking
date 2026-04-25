import sys

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    iterator = iter(input_data)
    
    try:
        n = int(next(iterator))
        t = int(next(iterator))
    except StopIteration:
        return

    up = [int(next(iterator)) for _ in range(n)]
    down = [int(next(iterator)) for _ in range(n)]
    
    diff = [0] * (n + 1)
    
    for _ in range(t):
        i = int(next(iterator))
        j = int(next(iterator))
        
        l = i - 1
        r = j - 1
        
        diff[l] += 1
        diff[r + 1] -= 1
        
    output = []
    current_flips = 0
    
    for i in range(n):
        current_flips += diff[i]
        
        if current_flips % 2 == 1:
            output.append(str(down[i]))
        else:
            output.append(str(up[i]))
            
    print(' '.join(output))

if __name__ == '__main__':
    main()