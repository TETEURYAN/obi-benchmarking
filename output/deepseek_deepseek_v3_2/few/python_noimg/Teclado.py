import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    
    N = data[0]
    M = int(data[1])
    strings = data[2:2+M]
    
    mapping = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz'
    }
    
    count = 0
    for s in strings:
        if len(s) != len(N):
            continue
        
        valid = True
        for i, ch in enumerate(s):
            digit = N[i]
            if ch not in mapping[digit]:
                valid = False
                break
        
        if valid:
            count += 1
    
    print(count)

if __name__ == "__main__":
    main()