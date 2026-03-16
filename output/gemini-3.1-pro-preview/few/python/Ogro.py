import sys

input_data = sys.stdin.read().split()
if len(input_data) >= 2:
    E = int(input_data[0])
    D = int(input_data[1])
    
    if E > D:
        print(E + D)
    else:
        print(2 * (D - E))