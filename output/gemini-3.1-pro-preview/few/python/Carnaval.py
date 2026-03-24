import sys

input_data = sys.stdin.read().split()
if not input_data:
    exit()

scores = sorted(float(x) for x in input_data)
final_score = sum(scores[1:4])

print(f"{final_score:.1f}")