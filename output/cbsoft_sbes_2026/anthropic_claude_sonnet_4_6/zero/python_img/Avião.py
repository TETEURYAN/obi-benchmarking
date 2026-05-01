F, C, E, B = map(int, input().split())

eco_rows = F - E + 1
total_seats = eco_rows * C

if B > total_seats:
    print("PROXIMO VOO")
else:
    row_index = (B - 1) // C
    col_index = (B - 1) % C
    row = E + row_index
    col = chr(ord('A') + col_index)
    print(row, col)