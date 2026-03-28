import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    
    E = int(data[0])
    D = int(data[1])
    
    if E > D:
        print(E + D)
    else:
        print(2 * (D - E))

if __name__ == "__main__":
    main()