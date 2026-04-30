import sys

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    H = int(input_data[0])
    P = int(input_data[1])
    F = int(input_data[2])
    D = int(input_data[3])
    
    curr = F
    while True:
        if curr == H:
            print("S")
            break
        if curr == P:
            print("N")
            break
        curr = (curr + D) % 16

if __name__ == '__main__':
    main()