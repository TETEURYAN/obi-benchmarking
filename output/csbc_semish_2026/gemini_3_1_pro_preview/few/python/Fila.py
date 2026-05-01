import sys

input_data = sys.stdin.read().split()
if not input_data:
    exit()

n = int(input_data[0])
initial_queue = input_data[1:n+1]
m = int(input_data[n+1])
left_queue = set(input_data[n+2:n+2+m])

result = [person for person in initial_queue if person not in left_queue]

print(" ".join(result))