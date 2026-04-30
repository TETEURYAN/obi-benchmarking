import sys

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    
    max_so_far = int(input_data[1])
    current_max = int(input_data[1])
    
    for i in range(2, n + 1):
        val = int(input_data[i])
        if current_max < 0:
            current_max = val
        else:
            current_max += val
            
        if current_max > max_so_far:
            max_so_far = current_max
            
    print(max_so_far)

if __name__ == '__main__':
    main()