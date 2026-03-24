import sys

input_data = sys.stdin.read().split()
if not input_data:
    exit()

S = [int(x) for x in input_data]

trophies = S.count(S[0])
if trophies == 5:
    plaques = 0
else:
    plaques = S.count(S[trophies])

print(f"{trophies} {plaques}")