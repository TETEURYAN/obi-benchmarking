import sys

input_data = sys.stdin.read().split()
if len(input_data) < 5:
    exit()

box = sorted([int(input_data[0]), int(input_data[1]), int(input_data[2])])
window = sorted([int(input_data[3]), int(input_data[4])])

if box[0] <= window[0] and box[1] <= window[1]:
    print('S')
else:
    print('N')