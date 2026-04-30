import sys

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    m = int(input_data[1])
    
    col_sums = [0] * m
    
    idx = 2
    for _ in range(n):
        for j in range(m):
            col_sums[j] += int(input_data[idx])
            idx += 1
            
    print(min(col_sums))

if __name__ == '__main__':
    main()