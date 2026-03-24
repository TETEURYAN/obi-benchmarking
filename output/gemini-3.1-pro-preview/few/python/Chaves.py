import sys

def solve():
    lines = sys.stdin.read().splitlines()
    if not lines:
        return
    
    balance = 0
    for line in lines[1:]:
        for char in line:
            if char == '{':
                balance += 1
            elif char == '}':
                balance -= 1
                if balance < 0:
                    print("N")
                    return
                    
    if balance == 0:
        print("S")
    else:
        print("N")

if __name__ == '__main__':
    solve()