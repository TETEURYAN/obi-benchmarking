import sys

input_data = sys.stdin.read().split()
if not input_data:
    sys.exit()

n = int(input_data[0])
if n == 1:
    print(1)
    sys.exit()

seq = [int(x) for x in input_data[1:n+1]]

count = 1
diff = seq[1] - seq[0]
for i in range(2, n):
    current_diff = seq[i] - seq[i-1]
    if current_diff != diff:
        count += 1
        diff = current_diff

print(count)