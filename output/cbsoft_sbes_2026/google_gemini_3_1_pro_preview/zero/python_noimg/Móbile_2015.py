import sys

def solve():
    input_data = sys.stdin.read().split()
    if len(input_data) >= 4:
        a = int(input_data[0])
        b = int(input_data[1])
        c = int(input_data[2])
        d = int(input_data[3])
        
        if a == b + c + d and b + c == d and b == c:
            print("S")
        else:
            print("N")

if __name__ == '__main__':
    solve()