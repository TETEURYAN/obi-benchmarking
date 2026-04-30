import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    seen = set()
    
    for i in range(1, len(input_data) - 1, 2):
        x = int(input_data[i])
        y = int(input_data[i+1])
        
        val = (x << 32) | y
        if val in seen:
            print(1)
            return
        seen.add(val)
        
    print(0)

if __name__ == '__main__':
    solve()