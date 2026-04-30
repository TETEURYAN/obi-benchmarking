import sys

def main():
    entrada = sys.stdin.read().split()
    if len(entrada) >= 3:
        L = int(entrada[0])
        R = int(entrada[1])
        D = int(entrada[2])
        
        if R > 50 and L < R and R > D:
            print("S")
        else:
            print("N")

if __name__ == '__main__':
    main()