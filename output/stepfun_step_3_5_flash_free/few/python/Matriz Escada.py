import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    
    n = int(data[0])
    m = int(data[1])
    matrix = []
    idx = 2
    for i in range(n):
        row = list(map(int, data[idx:idx+m]))
        matrix.append(row)
        idx += m
    
    pivot_col = -1
    zero_row_found = False
    
    for i in range(n):
        row = matrix[i]
        j = 0
        while j < m and row[j] == 0:
            j += 1
        if j == m:
            zero_row_found = True
        else:
            if zero_row_found:
                print('N')
                return
            if j <= pivot_col:
                print('N')
                return
            pivot_col = j
    
    print('S')

if __name__ == "__main__":
    main()