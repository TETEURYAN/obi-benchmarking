import sys

input_data = sys.stdin.read().split()
if not input_data:
    exit()

v_count = input_data.count('V')

if v_count >= 5:
    print(1)
elif v_count >= 3:
    print(2)
elif v_count >= 1:
    print(3)
else:
    print(-1)