
D = int(input())
pos = (D + 200) // 400 * 400
if pos > 2000:
    pos = 2000
print(abs(D - pos))
