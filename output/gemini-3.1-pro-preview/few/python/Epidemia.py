import sys

input_data = sys.stdin.read().split()
if not input_data:
    exit()

n = int(input_data[0])
r = int(input_data[1])
p = int(input_data[2])

total_infected = n
newly_infected = n
days = 0

while total_infected < p:
    newly_infected *= r
    total_infected += newly_infected
    days += 1

print(days)