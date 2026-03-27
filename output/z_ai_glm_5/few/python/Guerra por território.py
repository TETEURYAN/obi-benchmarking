import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    sections = list(map(int, input_data[1:n+1]))
    
    total_sum = sum(sections)
    current_sum = 0
    
    for i in range(n):
        current_sum += sections[i]
        if current_sum * 2 == total_sum:
            print(i + 1)
            return

if __name__ == '__main__':
    solve()