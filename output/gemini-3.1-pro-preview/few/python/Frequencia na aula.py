import sys

input_data = sys.stdin.read().split()
if input_data:
    n = int(input_data[0])
    unique_students = set(int(x) for x in input_data[1:n+1])
    print(len(unique_students))