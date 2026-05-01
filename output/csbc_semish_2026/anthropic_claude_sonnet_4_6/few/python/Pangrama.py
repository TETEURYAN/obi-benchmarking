import sys

line = sys.stdin.readline().rstrip('\n')
alphabet = set('abcdefghijlmnopqrstuvxz')
found = set(c for c in line if c in alphabet)
print('S' if found == alphabet else 'N')