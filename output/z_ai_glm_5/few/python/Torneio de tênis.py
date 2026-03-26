import sys

def solve():
    input_data = sys.stdin.read().split()
    
    wins = input_data.count('V')
    
    if wins >= 5:
        print(1)
    elif wins >= 3:
        print(2)
    elif wins >= 1:
        print(3)
    else:
        print(-1)

if __name__ == "__main__":
    solve()