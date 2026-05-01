import sys

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    E1 = int(data[0])
    E2 = int(data[1])
    E3 = int(data[2])
    X = int(data[3])
    
    if E2 - E1 <= X:
        print(E2)
    else:
        print(E3)

if __name__ == "__main__":
    main()