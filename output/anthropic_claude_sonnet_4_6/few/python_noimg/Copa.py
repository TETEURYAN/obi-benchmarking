import sys

data = sys.stdin.read().split()
k = int(data[0])
l = int(data[1])

# Convert to 0-indexed
k -= 1
l -= 1

round_num = 0
while k // (2 ** (round_num + 1)) != l // (2 ** (round_num + 1)):
    round_num += 1

if round_num == 0:
    print("oitavas")
elif round_num == 1:
    print("quartas")
elif round_num == 2:
    print("semifinal")
else:
    print("final")