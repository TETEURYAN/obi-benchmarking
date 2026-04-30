import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    N = int(input_data[0])
    
    total = 7
    
    if N > 100:
        total += (N - 100) * 5
        total += 70 * 2
        total += 20 * 1
    elif N > 30:
        total += (N - 30) * 2
        total += 20 * 1
    elif N > 10:
        total += (N - 10) * 1
        
    print(total)

if __name__ == '__main__':
    solve()