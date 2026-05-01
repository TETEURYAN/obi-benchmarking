import sys

input_data = sys.stdin.read().split()
if not input_data:
    exit()

count = 0

for row in input_data:
    for i in range(5):
        if row[i:i+3] == "oo." or row[i:i+3] == ".oo":
            count += 1

for j in range(7):
    col = "".join(input_data[i][j] for i in range(7))
    for i in range(5):
        if col[i:i+3] == "oo." or col[i:i+3] == ".oo":
            count += 1

print(count)