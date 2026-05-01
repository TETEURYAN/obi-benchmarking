import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    F = int(input_data[0])
    R = int(input_data[1])
    
    positions = [int(x) for x in input_data[2:2+R]]
    
    max_days = positions[0] - 1
    
    for i in range(1, R):
        days = (positions[i] - positions[i-1]) // 2
        if days > max_days:
            max_days = days
            
    if F - positions[-1] > max_days:
        max_days = F - positions[-1]
        
    print(max_days)

if __name__ == '__main__':
    solve()