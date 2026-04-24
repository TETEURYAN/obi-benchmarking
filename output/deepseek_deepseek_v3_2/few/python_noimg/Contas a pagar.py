import sys

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    
    V = int(data[0])
    A = int(data[1])
    F = int(data[2])
    P = int(data[3])
    
    bills = [A, F, P]
    bills.sort()
    
    count = 0
    remaining = V
    for bill in bills:
        if remaining >= bill:
            remaining -= bill
            count += 1
    
    print(count)

if __name__ == "__main__":
    main()