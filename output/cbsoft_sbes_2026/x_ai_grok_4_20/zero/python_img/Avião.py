
import sys

input = sys.stdin.read
data = input().strip().split()
F = int(data[0])
C = int(data[1])
E = int(data[2])
B = int(data[3])

rows_econ = F - E + 1
total_seats = rows_econ * C

if B > total_seats:
    print("PROXIMO VOO")
else:
    pos = B - 1
    row_offset = pos // C
    seat_idx = pos % C
    row = E + row_offset
    letter = chr(ord('A') + seat_idx)
    print(row, letter)
