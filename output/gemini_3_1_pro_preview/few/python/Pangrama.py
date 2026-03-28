import sys

text = sys.stdin.read()
alphabet = "abcdefghijlmnopqrstuvxz"

for c in alphabet:
    if c not in text:
        print("N")
        break
else:
    print("S")