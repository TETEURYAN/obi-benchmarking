import sys
notes = list(map(float, sys.stdin.read().split()))
notes.sort()
result = sum(notes[1:4])
print(f"{result:.1f}")