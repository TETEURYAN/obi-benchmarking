import sys

def solve():
    data = sys.stdin.read().split()
    
    if not data:
        return

    n1 = int(data[0])
    d1 = int(data[1])
    v1 = int(data[2])
    
    n2 = int(data[3])
    d2 = int(data[4])
    v2 = int(data[5])
    
    # Time = Distance / Velocity
    # To avoid floating point errors, we compare D1/V1 with D2/V2
    # by cross-multiplying: D1*V2 < D2*V1
    # This checks if chariot 1 takes less time than chariot 2.
    
    if d1 * v2 < d2 * v1:
        print(n1)
    else:
        print(n2)

if __name__ == '__main__':
    solve()