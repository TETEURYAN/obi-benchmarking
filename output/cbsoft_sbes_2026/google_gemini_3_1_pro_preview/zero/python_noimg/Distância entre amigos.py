import sys

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    N = int(input_data[0])
    
    max_val = int(input_data[1]) - 1
    max_dist = 0
    
    for j in range(1, N):
        aj = int(input_data[j + 1])
        current_dist = max_val + aj + (j + 1)
        if current_dist > max_dist:
            max_dist = current_dist
        
        current_val = aj - (j + 1)
        if current_val > max_val:
            max_val = current_val
            
    print(max_dist)

if __name__ == '__main__':
    main()