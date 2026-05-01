import sys

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    last_seen = int(input_data[1])
    count = 1
    
    for i in range(2, n + 1):
        current = int(input_data[i])
        if current != last_seen:
            count += 1
            last_seen = current
            
    print(count)

if __name__ == '__main__':
    main()