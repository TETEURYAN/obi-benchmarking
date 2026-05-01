import sys

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    
    max_h = 0
    seen = 0
    for i in range(n, 0, -1):
        h = int(input_data[i])
        if h > max_h:
            seen += 1
            max_h = h
            
    print(n - seen)

if __name__ == '__main__':
    main()