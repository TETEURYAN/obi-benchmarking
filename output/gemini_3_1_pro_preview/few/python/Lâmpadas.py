import sys

input_data = sys.stdin.read().split()
if input_data:
    n = int(input_data[0])
    count_2 = input_data[1:n+1].count('2')
    print(n % 2)
    print(count_2 % 2)