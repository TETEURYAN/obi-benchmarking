import sys

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    seen = set()
    
    for i in range(1, 2 * n, 2):
        x = int(input_data[i])
        y = int(input_data[i+1])
        
        if (x, y) in seen:
            print(1)
            return
        seen.add((x, y))
        
    print(0)

if __name__ == '__main__':
    main()