import sys

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    H, P, F, D = map(int, input_data)
    
    while True:
        if F == H:
            print("S")
            break
        if F == P:
            print("N")
            break
        F = (F + D) % 16

if __name__ == '__main__':
    main()