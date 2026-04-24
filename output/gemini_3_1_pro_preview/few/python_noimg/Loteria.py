import sys

input_data = sys.stdin.read().split()
if not input_data:
    exit()

bet = set(input_data[:6])
drawn = set(input_data[6:12])

matches = len(bet & drawn)

if matches == 3:
    print("terno")
elif matches == 4:
    print("quadra")
elif matches == 5:
    print("quina")
elif matches == 6:
    print("sena")
else:
    print("azar")