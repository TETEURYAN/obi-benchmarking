import sys

input_data = sys.stdin.read().split()
if input_data:
    e1 = int(input_data[0])
    e2 = int(input_data[1])
    e3 = int(input_data[2])
    x = int(input_data[3])
    
    if e2 - e1 <= x:
        print(e2)
    else:
        print(e3)