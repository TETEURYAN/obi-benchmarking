F, C, E, B = map(int, input().split())

eco_rows = F - E + 1
total_seats = eco_rows * C

if B > total_seats:
    print("PROXIMO VOO")
else:
    row_offset = (B - 1) // C
    col_offset = (B - 1) % C
    row = E + row_offset
    col = chr(ord('A') + col_offset)
    print(row, col)