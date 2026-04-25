import sys

input_data = sys.stdin.read().split()
T1 = int(input_data[0])
T2 = int(input_data[1])
T3 = int(input_data[2])

athletes = [(T1, 1), (T2, 2), (T3, 3)]
sorted_athletes = sorted(athletes)

print(sorted_athletes[0][1])
print(sorted_athletes[1][1])
print(sorted_athletes[2][1])