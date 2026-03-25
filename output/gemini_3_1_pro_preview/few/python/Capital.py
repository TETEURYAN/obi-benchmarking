import sys

input_data = sys.stdin.read().split()
if input_data:
    areas = sorted(map(int, input_data[:4]))
    if areas[0] * areas[3] == areas[1] * areas[2]:
        print('S')
    else:
        print('N')