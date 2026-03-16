import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    k = int(input_data[1])
    a = sorted((int(x) for x in input_data[2:]), reverse=True)
    
    if k > 0:
        print(a[k-1])

if __name__ == '__main__':
    solve()