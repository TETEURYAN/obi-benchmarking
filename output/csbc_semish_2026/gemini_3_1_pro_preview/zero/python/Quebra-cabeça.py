import sys

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    
    next_piece = {}
    char_piece = {}
    
    idx = 1
    for _ in range(n):
        e = int(input_data[idx])
        c = input_data[idx+1]
        d = int(input_data[idx+2])
        idx += 3
        
        next_piece[e] = d
        char_piece[e] = c
        
    curr = 0
    ans = []
    while curr != 1:
        ans.append(char_piece[curr])
        curr = next_piece[curr]
        
    print("".join(ans))

if __name__ == '__main__':
    main()