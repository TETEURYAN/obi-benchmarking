import sys

def main():
    input_data = sys.stdin.read().split()
    if len(input_data) < 2:
        return
    
    H = input_data[0]
    V = input_data[1]
    
    last_pos = {}
    for j, char in enumerate(V):
        last_pos[char] = j + 1
        
    for i in range(len(H) - 1, -1, -1):
        if H[i] in last_pos:
            print(f"{i + 1} {last_pos[H[i]]}")
            return
            
    print("-1 -1")

if __name__ == '__main__':
    main()