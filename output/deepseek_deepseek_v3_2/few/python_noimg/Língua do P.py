import sys

line = sys.stdin.readline().rstrip('\n')
result = []
i = 0
while i < len(line):
    if line[i] == 'p':
        i += 1
        if i < len(line) and line[i] != ' ':
            result.append(line[i])
            i += 1
    else:
        result.append(line[i])
        i += 1
print(''.join(result))