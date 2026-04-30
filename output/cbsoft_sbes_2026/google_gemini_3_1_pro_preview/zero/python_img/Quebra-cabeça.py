import sys

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    
    pieces = {}
    idx = 1
    for _ in range(n):
        e = int(input_data[idx])
        c = input_data[idx+1]
        d = int(input_data[idx+2])
        pieces[e] = (c, d)
        idx += 3
        
    curr = 0
    result = []
    for _ in range(n):
        c, d = pieces[curr]
        result.append(c)
        curr = d
        
    sys.stdout.write("".join(result) + "\n")

if __name__ == '__main__':
    main()