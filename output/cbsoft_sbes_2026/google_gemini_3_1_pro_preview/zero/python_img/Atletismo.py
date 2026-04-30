import sys

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    pos = [0] * (n + 1)
    
    for i in range(1, n + 1):
        athlete = int(input_data[i])
        pos[athlete] = i
        
    out = [str(pos[i]) for i in range(1, n + 1)]
    print('\n'.join(out))

if __name__ == '__main__':
    main()