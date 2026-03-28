import sys

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    
    max_val = int(input_data[1]) - 1
    ans = 0
    
    for j in range(1, n):
        aj = int(input_data[j + 1])
        current_val = max_val + aj + j + 1
        if current_val > ans:
            ans = current_val
        
        val_j = aj - j - 1
        if val_j > max_val:
            max_val = val_j

    print(ans)

if __name__ == '__main__':
    main()