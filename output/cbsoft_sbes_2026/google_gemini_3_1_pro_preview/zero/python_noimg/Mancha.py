
import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    N = int(input_data[0])
    grid = input_data[1:N+1]
    
    # Verifica se todas as linhas são contíguas
    for r in range(N):
        row = grid[r]
        first = row.find('*')
        if first != -1:
            last = row.rfind('*')
            count = row.count('*')
            if count != (last - first + 1):
                print("N")
                return
                
    # Verifica se todas as colunas são contíguas
    for c in range(N):
        first = -1
        last = -1
        count = 0
        for r in range(N):
            if grid[r][c] == '*':
                if first == -1:
                    first = r
                last = r
                count += 1
        if count > 0 and count != (last - first + 1):
            print("N")
            return
            
    print("S")

if __name__ == '__main__':
    solve()
