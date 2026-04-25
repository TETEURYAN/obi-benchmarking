import sys

input_data = sys.stdin.read().split()
if not input_data:
    exit()

n = int(input_data[0])
strings = input_data[1:]

seen_strings = set()
seen_prefixes = set()
seen_suffixes = set()

for s in strings:
    if s in seen_strings:
        print(s)
        exit()
    
    for i in range(1, 10):
        if s[:i] in seen_suffixes and s[i:] in seen_prefixes:
            print(s)
            exit()
            
    seen_strings.add(s)
    for i in range(1, 10):
        seen_prefixes.add(s[:i])
        seen_suffixes.add(s[i:])

print("ok")