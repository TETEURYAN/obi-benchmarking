import sys

input_data = sys.stdin.read().split()
if input_data:
    ages = sorted(int(x) for x in input_data[:3])
    print(ages[1])