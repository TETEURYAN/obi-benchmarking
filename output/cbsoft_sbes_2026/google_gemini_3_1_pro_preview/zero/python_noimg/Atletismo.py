import sys

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    N = int(input_data[0])
    pos = [0] * (N + 1)
    
    for i in range(1, N + 1):
        pos[int(input_data[i])] = i
        
    sys.stdout.write('\n'.join(map(str, pos[1:])) + '\n')

if __name__ == '__main__':
    main()