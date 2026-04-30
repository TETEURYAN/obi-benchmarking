import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    N = input_data[0]
    M = int(input_data[1])
    strings = input_data[2:2+M]
    
    mapping = {
        'a': '2', 'b': '2', 'c': '2',
        'd': '3', 'e': '3', 'f': '3',
        'g': '4', 'h': '4', 'i': '4',
        'j': '5', 'k': '5', 'l': '5',
        'm': '6', 'n': '6', 'o': '6',
        'p': '7', 'q': '7', 'r': '7', 's': '7',
        't': '8', 'u': '8', 'v': '8',
        'w': '9', 'x': '9', 'y': '9', 'z': '9'
    }
    
    count = 0
    len_N = len(N)
    for s in strings:
        if len(s) != len_N:
            continue
        match = True
        for i in range(len_N):
            if mapping[s[i]] != N[i]:
                match = False
                break
        if match:
            count += 1
            
    print(count)

if __name__ == '__main__':
    solve()