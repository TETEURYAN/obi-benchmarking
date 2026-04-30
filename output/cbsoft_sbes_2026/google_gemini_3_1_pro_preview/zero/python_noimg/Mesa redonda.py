import sys

def main():
    input_data = sys.stdin.read().split()
    if len(input_data) >= 2:
        a = int(input_data[0])
        b = int(input_data[1])
        
        ca = a % 3
        cb = b % 3
        
        if cb == ca:
            cb = (cb + 1) % 3
            
        cc = 3 - ca - cb
        print(cc)

if __name__ == '__main__':
    main()