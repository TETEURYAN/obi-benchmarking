import sys

input_data = sys.stdin.read().split()
if input_data:
    c = int(input_data[1])
    m = int(input_data[2])
    
    stamped = set(input_data[3:3+c])
    bought = set(input_data[3+c:3+c+m])
    
    print(len(stamped - bought))