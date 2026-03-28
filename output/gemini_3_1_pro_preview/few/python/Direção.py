import sys

input_data = sys.stdin.read().split()
if not input_data:
    exit()

a = input_data[0]
b = input_data[1]

dirs = {
    "norte": 0,
    "leste": 90,
    "sul": 180,
    "oeste": 270
}

diff = abs(dirs[a] - dirs[b])
print(min(diff, 360 - diff))