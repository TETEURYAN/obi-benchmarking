
import sys

def solve():
    data = sys.stdin.read().split()
    if len(data) < 4:
        return
    
    alphabet = set(data[2])
    message = data[3]
    
    if all(c in alphabet for c in message):
        print('S')
    else:
        print('N')

if __name__ == '__main__':
    solve()
