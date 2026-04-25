import sys

s = sys.stdin.readline().rstrip('\n')
alphabet = set("abcdefghijlmnopqrstuvxz")
letters = set(ch for ch in s if ch in alphabet)
print('S' if letters == alphabet else 'N')